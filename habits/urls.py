from django.urls import path

from habits.views import HabitUserListAPIView, HabitPublicListAPIView, HabitAllListAPIView, HabitCreateAPIView, \
    HabitRetrieveAPIView, HabitUpdateAPIView, HabitDeleteAPIView
from habits.apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitUserListAPIView.as_view(), name='habit-user-list'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-retrieve'),
    path('<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('<int:pk>/delete/', HabitDeleteAPIView.as_view(), name='habit-delete'),
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('public/', HabitPublicListAPIView.as_view(), name='habit-public-list'),
    path('admin/', HabitAllListAPIView.as_view(), name='habit-all-list'),
]
