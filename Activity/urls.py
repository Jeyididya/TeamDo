from django.urls import path
from .views import ActivityListCreateView, ActivityDetailView

app_name = 'activity'

urlpatterns = [
    path('activities/', ActivityListCreateView.as_view(),
         name='activity-list-create'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(),
         name='activity-detail'),
]
