from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.db.models import Q
from rest_framework.response import Response


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


class CompletedTaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(Q(is_completed=True) & Q(assigned_to=self.request.user))


class NonCompletedTaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(Q(is_completed=False) & Q(assigned_to=self.request.user))


# class TaskAssignView(generics.UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.assigned_by = request.user
#         instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)


class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_completed = True  # Mark the task as completed
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
