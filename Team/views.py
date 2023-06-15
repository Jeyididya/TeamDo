from datetime import datetime, timedelta
import os
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Team
from .serializers import TeamSerializer, InvitationSerializer
from django.conf import settings
from django.contrib.auth import get_user_model
from Invitation.models import Invitation
from Notification.models import Notification
from dotenv import load_dotenv
load_dotenv()


class TeamListCreateView(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Team.objects.filter(Q(members=user) | Q(public=True))


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


User = get_user_model()


class TeamInviteView(generics.CreateAPIView):
    serializer_class = InvitationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        team = self.get_team()
        if not team.members.filter(id=self.request.user.id).exists():
            raise PermissionDenied(
                'You must be a member of the team to invite someone.',
            )
        invited_users = self.get_invited_users()
        current_date = datetime.now().date()
        invitations = []
        for user in invited_users:
            try:

                invitation = Invitation.objects.create(
                    sender=self.request.user,
                    reciver=user,
                    team=team,
                    status='pending',
                    expiration_date=current_date +
                    timedelta(days=int(os.getenv('EXPIRATION_DATE')))
                )

                notification = Notification.objects.create(
                    user=user,
                    message=f'{self.request.user.first_name} invited you to {team}',
                )

            except User.DoesNotExist:
                return Response(
                    {'detail': 'No Valid Recipients found'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            invitations.append(invitation)
            # team.members.add(user)
        # print("-->", invitations)
        serializer.create(invitations)

    def get_team(self):
        team_id = self.kwargs['team_id']
        return Team.objects.get(id=team_id)

    def get_invited_users(self):
        invited_user_ids = self.request.data.get('reciver', [])
        print(invited_user_ids)
        return User.objects.filter(id__in=invited_user_ids)
