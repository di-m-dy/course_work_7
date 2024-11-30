import datetime

from celery import shared_task

from config.settings import ZONE
from habits.models import Habit, Report
from habits.services import send_tg_habit_notification


@shared_task
def check_habits():
    """
    Периодическая задача, которая проверяет все привычки.
    Отправляет уведомления о тех, которые должны быть выполнены
    """
    PERIOD_TIMEDELTA = {
        'day': datetime.timedelta(days=1),
        'week': datetime.timedelta(weeks=1)
    }
    NOW = datetime.datetime.now(ZONE)
    habits = Habit.objects.filter(period__isnull=False, is_nice_habit=False)
    for habit in habits:
        if habit.reports.all():
            last_report = habit.reports.all().order_by('-created_at').first()
            if last_report:
                if last_report.next_send + PERIOD_TIMEDELTA[habit.period] < NOW:
                    response = send_tg_habit_notification(habit)
                    if response.status_code == 200:
                        Report.objects.create(
                            habit=habit,
                            is_success=True,
                            next_send=last_report.created_at + PERIOD_TIMEDELTA[habit.period]
                        )
                    else:
                        Report.objects.create(
                            habit=habit,
                            is_success=False,
                            report=response.text,
                            next_send=last_report.created_at + PERIOD_TIMEDELTA[habit.period]
                        )
        else:
            if habit.date_time < NOW:
                response = send_tg_habit_notification(habit)
                if response.status_code == 200:
                    Report.objects.create(
                        habit=habit,
                        is_success=True,
                        next_send=habit.date_time + PERIOD_TIMEDELTA[habit.period]
                    )
                else:
                    Report.objects.create(
                        habit=habit,
                        is_success=False,
                        next_send=habit.date_time + PERIOD_TIMEDELTA[habit.period],
                        report=response.text
                    )
