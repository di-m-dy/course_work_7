from django.urls import path

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView, \
    UserRetrieveAPIView, UserDestroyAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user-delete'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]