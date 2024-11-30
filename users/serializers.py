from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """
    Сериализатор для пользователя
    """

    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(ModelSerializer):
    """
    Сериализатор для списка пользователей
    """

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(ModelSerializer):
    """
    Сериализатор для создания пользователя
    """

    class Meta:
        model = User
        fields = ('email', 'password', 'tg_id')
