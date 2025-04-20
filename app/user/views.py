from rest_framework import generics, authentication, permissions
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = UserSerializer.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManagerUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_calss = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
