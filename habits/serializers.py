from rest_framework.serializers import ModelSerializer

from habits.models import Habit, Report
from habits.validators import LinkedHabitRemunerationValidator, UsefulHabitRequiredFields, TimeToDoneValidator


class HabitNiceSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = ('action', 'place', 'is_public')

class HabitSerializer(ModelSerializer):
    linked_habit = HabitNiceSerializer()

    class Meta:
        model = Habit
        fields = '__all__'

class HabitCreateSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'id',
            'action',
            'place',
            'date_time',
            'is_nice_habit',
            'linked_habit',
            'period',
            'remuneration',
            'time_to_done',
            'is_public'
        )
        validators = [
            LinkedHabitRemunerationValidator(
                linked_habit_field='linked_habit',
                remuneration_field='remuneration'
            ),
            UsefulHabitRequiredFields(*fields),
            TimeToDoneValidator(time_to_done_field='time_to_done')
        ]


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'