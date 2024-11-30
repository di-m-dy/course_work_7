from django.core.exceptions import ValidationError


class LinkedHabitRemunerationValidator:
    """
    Пользовательский валидатор для проверки одновременного выбора связанных привычек и поощрений
    """

    def __init__(self, linked_habit_field, remuneration_field):
        self.linked_habit_field = linked_habit_field
        self.remuneration_field = remuneration_field

    def __call__(self, value):
        if value.get(self.linked_habit_field) and value.get(self.remuneration_field):
            raise ValidationError(f"Нельзя одновременно указывать связанную привычку и поощрение")
        if not value.get(self.linked_habit_field) and not value.get(self.remuneration_field):
            raise ValidationError(f"Необходимо указать связанную привычку или поощрение")


class UsefulHabitRequiredFields:
    """
    Если привычка полезная, то должна принимать обязательные поля:
        "place"
        "date_time"
        "period"
        "remuneration"/"linked_habit"
        "time_to_done": 60,
        "is_public": false
    Проверка чтобы связанная привычка не имела связанных привычек и поощрения
    """

    def __init__(self, *args):
        self.fields = args

    def __call__(self, value):
        fields = [
            value.get('place'),
            value.get('date_time'),
            value.get('period'),
            value.get('remuneration') or value.get('linked_habit'),
            value.get('time_to_done')
        ]
        if not value.get('is_nice_habit') and not all(fields):
            raise ValidationError(f"Проверьте, что все обязательные поля заполнены: "
                                  f"place, date_time, period, remuneration/linked_habit, time_to_done, is_public")
        if value.get('is_nice_habit') and (value.get('linked_habit') or value.get('remuneration')):
            raise ValidationError(f"Связанная приятная привычка не может иметь связанные привычки или поощрение")


class TimeToDoneValidator:
    """
    Время выполнения должно быть не больше 120 секунд (поле: time_to_done)
    """

    def __init__(self, time_to_done_field):
        self.time_to_done_field = time_to_done_field

    def __call__(self, value):
        if value.get(self.time_to_done_field) and value.get(self.time_to_done_field) > 120:
            raise ValidationError("Время выполнения привычки не может быть дольше 2 минут (обратите внимание, что поле "
                                  "заполняется в секундах - таким образом, значение должно быть не больше 120)")
