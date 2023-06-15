from django.db import models
from django.conf import settings
# Create your models here.


class Invitation(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_invitations')
    reciver = models.ForeignKey(
        settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='recived_invitations')
    team = models.ForeignKey('Team.Team', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[(
        'pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField()

    def __str__(self):
        return f'{self.sender} - {self.reciver}-{self.team}'
