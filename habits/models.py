from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название привычки")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(
        max_length=150, verbose_name="Место выполнения", **NULLABLE
    )
    time_action = models.TimeField(verbose_name="Время когда нужно выполнить", **NULLABLE)
    action = models.CharField(max_length=250, verbose_name="Действие")
    pleasant = models.BooleanField(default=False, verbose_name="Приятная")
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE
    )
    period = models.PositiveIntegerField(default=1, verbose_name="Периодичность в днях")
    prize = models.CharField(max_length=150, verbose_name="Вознаграждение", **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name="Публичная")
    complete_time = models.IntegerField(verbose_name="Время на выполнение", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
