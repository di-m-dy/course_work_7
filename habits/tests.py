import datetime

from django.urls import reverse
from rest_framework.test import APITestCase

from habits.models import Habit, Report
from users.models import User


class HabitTestCase(APITestCase):
    """
    Тесты для привычек (CRUD)
    """

    def setUp(self):
        self.user = User.objects.create(
            email="test@example.com",
            tg_id=123,
            password="testpassword"
        )
        self.other_user = User.objects.create(
            email="other_test@example",
            tg_id=124,
            password="testpassword"
        )
        self.habit = Habit.objects.create(
            action="Test Action",
            user=self.user,
            is_nice_habit=False,
            is_public=False,
            period="day",
            time_to_done=60,
            place="Test Place",
            date_time="2021-01-01T00:00:00Z"
        )

        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit-retrieve", args=[self.habit.pk])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["action"], self.habit.action)
        self.assertEqual(data["user"], self.habit.user.pk)
        self.assertEqual(data["is_nice_habit"], self.habit.is_nice_habit)
        self.assertEqual(data["is_public"], self.habit.is_public)
        self.assertEqual(data["period"], self.habit.period)
        self.assertEqual(data["time_to_done"], self.habit.time_to_done)
        self.assertEqual(data["place"], self.habit.place)
        self.assertEqual(data["date_time"], self.habit.date_time)

    def test_habit_create(self):
        url = reverse("habits:habit-create")
        data = {
            "action": "New Action",
            "is_nice_habit": False,
            "is_public": False,
            "period": "week",
            "time_to_done": 120,
            "place": "New Place",
            "date_time": "2021-01-01T00:00:00Z",
            "remuneration": "New Remuneration"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Habit.objects.count(), 2)
        self.assertEqual(Habit.objects.last().action, "New Action")
        self.assertEqual(Habit.objects.last().user, self.user)
        self.assertEqual(Habit.objects.last().is_nice_habit, False)
        self.assertEqual(Habit.objects.last().is_public, False)
        self.assertEqual(Habit.objects.last().period, "week")
        self.assertEqual(Habit.objects.last().time_to_done, 120)
        self.assertEqual(Habit.objects.last().place, "New Place")
        self.assertEqual(Habit.objects.last().date_time,
                         datetime.datetime.fromisoformat("2021-01-01T00:00:00").astimezone())

    def test_habit_update(self):
        url = reverse("habits:habit-update", args=[self.habit.pk])
        new_data = {
            "action": "New Action"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data=new_data)
        self.assertEqual(response.status_code, 200)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.action, "New Action")

    def test_habit_delete(self):
        url = reverse("habits:habit-delete", args=[self.habit.pk])
        self.client.force_authenticate(user=self.other_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 403)
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Habit.objects.count(), 0)

    def test_habit_user_list(self):
        url = reverse("habits:habit-user-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['results']), 1)
        self.assertEqual(data['results'][0]["action"], self.habit.action)
        self.assertEqual(data['results'][0]["user"], self.habit.user.pk)
        self.assertEqual(data['results'][0]["is_nice_habit"], self.habit.is_nice_habit)
        self.assertEqual(data['results'][0]["is_public"], self.habit.is_public)
        self.assertEqual(data['results'][0]["period"], self.habit.period)
        self.assertEqual(data['results'][0]["time_to_done"], self.habit.time_to_done)
        self.assertEqual(data['results'][0]["place"], self.habit.place)
        self.assertEqual(data['results'][0]["date_time"], self.habit.date_time)

    def test_habit_public_list(self):
        url = reverse("habits:habit-public-list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 0)
