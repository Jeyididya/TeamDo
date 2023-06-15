from django.db import models
from django.conf import settings


class Project(models.Model):
    team = models.ForeignKey('Team.Team', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='projects')
