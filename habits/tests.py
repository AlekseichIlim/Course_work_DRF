from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование CRUD привычек"""

    def setUp(self):
        self.user = User.objects.create(email="admin@mail.ru")
        self.habit = Habit.objects.create(
            owner=self.user,
            title="Чтение",
            location="Дома",
            time_action="9:00",
            action="Прочитать 10 страниц",
            pleasant=False,
            period=1,
            prize="съесть конфету",
            is_public=False,
            complete_time=1,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):

        data = {
            "owner": self.user.pk,
            "title": "Чтение",
            "location": "Дома",
            "time_action": "9:00",
            "action": "Прочитать 10 страниц",
            "pleasant": "False",
            "period": 1,
            "prize": "съесть конфету",
            "is_public": "False",
            "complete_time": 1,
        }
        url = reverse('habits:habit_create')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.all().exists())

    def test_habit_retrieve(self):

        url = reverse('habits:habit_detail', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK,)
        self.assertTrue(Habit.objects.all().exists())

    def test_habit_update(self):

        url = reverse('habits:habit_update', args=(self.habit.pk,))
        data = {
            'title': '10 страниц',
            'complete_time': 2,
            'period': 1,

        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK,)
        self.assertTrue(Habit.objects.all().exists())
        self.assertEqual(data.get('title'), '10 страниц', )

    def test_habit_delete(self):

        url = reverse('habits:habit_delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):

        url = reverse('habits:habits_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, )

