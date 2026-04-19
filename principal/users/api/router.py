from django.urls import path
from rest_framework.routers import DefaultRouter
from users.api.views import UserViewSet

router_user = DefaultRouter()
router_user.register(prefix='users', viewset=UserViewSet)

urlpatterns = []  