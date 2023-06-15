from django.db import models
from django.conf import settings


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='teams')
    public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
