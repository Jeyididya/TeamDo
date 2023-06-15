from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListCreateView, UserDetailView

app_name = 'user'

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/token/', TokenObtainPairView.as_view(), name='user-token'),
    path('users/refresh/', TokenRefreshView.as_view(), name='user-refresh'),
]
