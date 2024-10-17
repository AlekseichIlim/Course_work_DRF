from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.serializers import ValidationError

from habits.models import Habit
from habits.paginations import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwnerPermission


class HabitCreateAPIView(CreateAPIView):
    """Создание привчки"""

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Назначение владельца привычки"""

        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitPublicListAPIView(ListAPIView):
    """Просмотр публичных привычек"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all().filter(is_public=True)
    pagination_class = CustomPagination


class MyHabitListAPIView(ListAPIView):
    """Просмотр привычек текущего пользователя"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitRetrieveAPIView(RetrieveAPIView):
    """Просмотр привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwnerPermission,)


class HabitUpdateAPIView(UpdateAPIView):
    """Изменение привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwnerPermission,)


class HabitDestroyAPIView(DestroyAPIView):
    """Удаление привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwnerPermission,)
