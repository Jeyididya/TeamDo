from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Invitation
from .serializers import InvitationSerializer
from Notification.models import Notification
from django.db.models import Q


class InvitationListCreateView(generics.ListCreateAPIView):
    serializer_class = InvitationSerializer

    def get_queryset(self):
        user = self.request.user
        print("-->", user, user.id)
        return Invitation.objects.filter(Q(sender=user) | Q(reciver=user))


class InvitationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer


class SentInvitationsListView(generics.ListAPIView):
    serializer_class = InvitationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Invitation.objects.filter(sender=user)


class ReceivedInvitationsListView(generics.ListAPIView):
    serializer_class = InvitationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Invitation.objects.filter(Q(reciver=user) & Q(status='pending'))


class AcceptInvitationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, invitation_id):
        try:
            invitation = Invitation.objects.get(
                id=invitation_id, status='pending', reciver=request.user)
        except Invitation.DoesNotExist:
            return Response({'detail': 'Invitation not found.'}, status=status.HTTP_404_NOT_FOUND)

        invitation.status = 'accepted'
        invitation.save()

        team = invitation.team
        team.members.add(request.user)

        Notification.objects.create(
            user=invitation.sender,
            message=f'{request.user} accepted your request to join {team}',
        )

        return Response({'detail': 'Invitation accepted.'}, status=status.HTTP_200_OK)
