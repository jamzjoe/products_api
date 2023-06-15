from django.contrib.auth import get_user_model
from rest_framework import generics
from user.serializers import UserSerializer

User = get_user_model()

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
