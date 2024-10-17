from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitPublicListAPIView, MyHabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("", HabitPublicListAPIView.as_view(), name="habits_list"),
    path("my/", MyHabitListAPIView.as_view(), name="my_habits_list"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_detail"),
    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit_delete"),
]
