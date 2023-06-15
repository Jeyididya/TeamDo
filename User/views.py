from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserLoginView(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})


# class UserLogoutView(APIView):
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             Token.objects.filter(user=request.user).delete()
#         return Response({'detail': 'Successfully logged out.'})
