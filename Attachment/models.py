from django.db import models
from django.conf import settings
# Create your models here.


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    task = models.ForeignKey(
        'Task.Task', on_delete=models.CASCADE, related_name='attachments')
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.task}-{self.file}'
