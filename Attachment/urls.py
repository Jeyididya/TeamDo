from django.urls import path
from .views import AttachmentListCreateView, AttachmentDetailView

app_name = 'attachment'

urlpatterns = [
    path('attachments/', AttachmentListCreateView.as_view(),
         name='attachment-list-create'),
    path('attachments/<int:pk>/', AttachmentDetailView.as_view(),
         name='attachment-detail'),
]
