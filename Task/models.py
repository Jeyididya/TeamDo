from django.db import models
from django.conf import settings


class Task(models.Model):
    project = models.ForeignKey(
        'Project.Project', on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_tasks')
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_bys', default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    attachment = models.ForeignKey(
        'Attachment.Attachment', on_delete=models.CASCADE, related_name='atachments', null=True, blank=True
    )

    def __str__(self):
        return f'{self.is_completed} - {self.assigned_by} -> {self.assigned_to}'
