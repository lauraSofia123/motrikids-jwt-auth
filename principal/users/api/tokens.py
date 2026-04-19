from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer personalizado que agrega claims adicionales al token JWT.
    El payload del token incluirá: username y role.
    """

    @classmethod
    def get_token(cls, user):
        # Generamos el token base (contiene user_id, exp, etc.)
        token = super().get_token(user)

        # --- Claims personalizados ---
        token['username'] = user.username
        token['role'] = 'admin' if user.is_staff else 'user'
        # -----------------------------

        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Vista que usa el serializer personalizado para devolver
    el token con los claims adicionales.
    """
    serializer_class = CustomTokenObtainPairSerializer
