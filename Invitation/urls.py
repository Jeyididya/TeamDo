from django.urls import path
from .views import InvitationListCreateView, InvitationDetailView, SentInvitationsListView, ReceivedInvitationsListView, AcceptInvitationView

app_name = 'invitation'

urlpatterns = [
    path('invitations/', InvitationListCreateView.as_view(),
         name='invitation-list-create'),
    path('invitations/<int:pk>/', InvitationDetailView.as_view(),
         name='invitation-detail'),
    path('invitations/sent/', SentInvitationsListView.as_view(),
         name='sent-invitations'),
    path('invitations/received/', ReceivedInvitationsListView.as_view(),
         name='received-invitations'),
    path('invitations/<int:invitation_id>/accept', AcceptInvitationView.as_view(),
         name='sent-invitations'),
]
