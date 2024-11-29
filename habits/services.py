import requests
from config.settings import TG_TOKEN
from habits.models import Habit


def send_tg_habit_notification(habit: Habit):
    tg_id = habit.user.tg_id
    message = (f"Я буду <b>ДЕЙСТВИЕ: {habit.action}</b>\nв <b>ВРЕМЯ: {habit.date_time}</b>\nв <b>МЕСТО: {habit.place}</b>\n"
               f"И за это мне будет: {habit.linked_habit if habit.linked_habit else habit.remuneration}")
    params = {
        "chat_id": tg_id,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.get(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", params=params)
    return response
