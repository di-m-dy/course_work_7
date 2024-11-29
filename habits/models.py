from django.db import models

from users.models import User


class Habit(models.Model):
    """
    Модель привычки
    Если привычка приятная, то в поле is_nice_habit ставим True и НЕ указываем поощрение и СВЯЗАННУЮ привычку
    Если привычка связана с другой привычкой, то в поле linked_habit указываем связанную привычку и НЕ указываем поощрение
    Если привычка публичная, то она отображается в общем списке привычек
    """
    PERIODS = (
        ('day', 'Ежедневно'),
        ('week', 'Еженедельно'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='habits'
    )
    action = models.CharField(max_length=500, verbose_name='Действие')
    place = models.CharField(max_length=500, verbose_name='Место', null=True, blank=True)
    date_time = models.DateTimeField(verbose_name='Дата и время', null=True, blank=True)
    is_nice_habit = models.BooleanField(verbose_name='Признак приятной привычки')
    linked_habit = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='Связанная привычка',
        related_name='linked_habits',
        null=True,
        blank=True
    )
    period = models.CharField(
        max_length=4,
        choices=PERIODS,
        verbose_name='Периодичность',
        null=True,
        blank=True
    )
    remuneration = models.CharField(max_length=500, verbose_name='Поощрение', null=True, blank=True)
    time_to_done = models.PositiveIntegerField(verbose_name='Время на выполнение (в секундах)', null=True, blank=True)
    is_public = models.BooleanField(verbose_name='Публичная привычка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

class Report(models.Model):
    """
    Модель отчета
    """
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        verbose_name='Привычка',
        related_name='reports'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_success = models.BooleanField(verbose_name='Выполнено')
    report = models.TextField(verbose_name='Отчет', null=True, blank=True)

    def __str__(self):
        return f"{self.habit} - {self.created_at}"

    class Meta:
        verbose_name = 'отчет'
        verbose_name_plural = 'отчеты'
