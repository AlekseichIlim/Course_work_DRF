from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("", HabitListAPIView.as_view(), name="lessons_list"),
]