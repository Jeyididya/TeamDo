from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from django.contrib.auth import get_user_model
from django.db.models import Q


class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        team_ids = self.request.user.teams.values_list('id', flat=True)

        return Project.objects.filter(Q(team_id__in=team_ids) | Q(members=self.request.user))


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
