from rest_framework import generics
from .models import Attachment
from .serializers import AttachmentSerializer


class AttachmentListCreateView(generics.ListCreateAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


class AttachmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
