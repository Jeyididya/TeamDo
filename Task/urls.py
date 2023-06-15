from django.urls import path
from .views import TaskListCreateView, TaskDetailView,  NonCompletedTaskListAPIView,  TaskUpdateView, CompletedTaskListAPIView

app_name = 'task'

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/not_completed/',
         NonCompletedTaskListAPIView.as_view(), name='task-detail'),
    path('tasks/completed/',
         CompletedTaskListAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', TaskUpdateView.as_view(), name='task-detail'),
]
