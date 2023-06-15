from django.db import models
from django.conf import settings
# Create your models here.


class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action_type = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return f'{self.user}- {self.action_type}'
