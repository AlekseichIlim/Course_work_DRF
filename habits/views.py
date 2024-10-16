from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.serializers import ValidationError

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Назначение владельца привычки"""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # pagination_class = CustomPagination