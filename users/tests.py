from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from users.models import User


class UserTestCase(APITestCase):
    """Тестирование CRUD пользователей"""

    def setUp(self):
        self.user = User.objects.create(email="admin@mail.ru")
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):

        data = {
            "email": "2@mail.ru",
            "password": 2002

        }
        url = reverse('users:user_register')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.all().exists())

    def test_user_retrieve(self):

        url = reverse('users:user_detail', args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK,)
        self.assertTrue(data.get('email'), self.user.email)

    def test_user_update(self):

        url = reverse('users:user_update', args=(self.user.pk,))
        data = {
            'email': '3@mail.ru',


        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK,)
        self.assertEqual(data.get('email'), '3@mail.ru', )

    def test_user_delete(self):

        url = reverse('users:user_delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)

    def test_user_list(self):

        url = reverse('users:user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, )
