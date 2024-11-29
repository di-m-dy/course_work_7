from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from habits.models import Habit
from habits.paginators import HabitUserListPagination
from habits.serializers import HabitSerializer, HabitCreateSerializer


class HabitCreateAPIView(CreateAPIView):
    """
    Создание привычки
    """
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUserListAPIView(ListAPIView):
    """
    Список пользователей
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitUserListPagination
    def get_queryset(self):
        user_list = Habit.objects.filter(user=self.request.user).order_by('-created_at')
        return user_list


class HabitPublicListAPIView(ListAPIView):
    """
    Список пользователей
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        public_list = Habit.objects.filter(is_public=True)
        return public_list

class HabitAllListAPIView(ListAPIView):
    """
    Список пользователей
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAdminUser]
    queryset = Habit.objects.all()

class HabitRetrieveAPIView(RetrieveAPIView):
    """
    Получение пользователя
    """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated] # todo: добавить права доступа для владельца привычки и админа
    serializer_class = HabitSerializer

class HabitUpdateAPIView(UpdateAPIView):
    """
    Обновление пользователя
    """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated] # todo: добавить права доступа для владельца привычки и админа
    serializer_class = HabitCreateSerializer

class HabitDeleteAPIView(DestroyAPIView):
    """
    Удаление пользователя
    """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated] # todo: добавить права доступа для владельца привычки и админа
    serializer_class = HabitSerializer




