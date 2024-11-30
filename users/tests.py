from django.urls import reverse
from rest_framework.test import APITestCase

from habits.models import Habit, Report
from users.models import User


class UserEndpointTestCase(APITestCase):
    """
    Тесты для пользователей (CRUD)
    """

    def setUp(self):
        self.user = User.objects.create(
            email="user_test@example.com",
            tg_id=123,
            password="testpassword"
        )
        self.other_user = User.objects.create(
            email="other_test@example",
            tg_id=124,
            password="testpassword"
        )

        self.client.force_authenticate(user=self.user)

    def test_user_retrieve(self):
        url = reverse("users:user-retrieve", args=[self.user.pk])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["email"], self.user.email)
        self.assertEqual(int(data["tg_id"]), self.user.tg_id)
        self.assertEqual(data["password"], self.user.password)

    #
    def test_user_create(self):
        url = reverse("users:user-create")
        data = {
            "email": "other_user_test@example.com",
            "tg_id": 125,
            "password": "testpassword"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(User.objects.last().email, "other_user_test@example.com")
        self.assertEqual(int(User.objects.last().tg_id), 125)
        self.assertEqual(User.objects.last().check_password("testpassword"), True)

    def test_user_update(self):
        url = reverse("users:user-update", args=[self.user.pk])
        data = {
            "tg_id": 126,
        }

        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(User.objects.get(pk=self.user.pk).tg_id), 126)

    def test_user_delete(self):
        url = reverse("users:user-delete", args=[self.user.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().email, self.other_user.email)
        self.assertEqual(int(User.objects.first().tg_id), self.other_user.tg_id)
        self.assertEqual(User.objects.first().password, self.other_user.password)

    def user_list(self):
        url = reverse("users:user-list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data, {"detail": "You do not have permission to perform this action."})
