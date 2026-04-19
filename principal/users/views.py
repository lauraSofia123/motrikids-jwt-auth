from rest_framework.viewsets import ModelViewSet
from users.models import User
from rest_framework.permissions import AllowAny
from users.api.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()