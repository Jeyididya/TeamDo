from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return f'{self.username}-{self.first_name}'
