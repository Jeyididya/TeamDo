from django.urls import path
from .views import TeamListCreateView, TeamDetailView,  TeamInviteView

app_name = 'team'

urlpatterns = [
    path('teams/', TeamListCreateView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('teams/<int:team_id>/invite/',
         TeamInviteView.as_view(), name='team-invite'),
]
