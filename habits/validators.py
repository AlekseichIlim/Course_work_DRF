from rest_framework import serializers
from rest_framework.serializers import ValidationError

from habits.models import Habit


class HabitsValidator:
    """Валидация полей привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value)
        if val.get("related_habit"):
            rel_hab = val.get("related_habit")
            id_rel_hab = rel_hab.id
            rel_hab = Habit.objects.all().get(pk=id_rel_hab)
            if rel_hab.pleasant is False:
                raise ValidationError(
                    f"Связанной привычкой может быть только приятная привычка!"
                )
        if val.get("complete_time") > 2:
            raise ValidationError("Время выполнения должно быть не более 2 минут!")
        elif val.get("pleasant") is False and (
            val.get("related_habit") and val.get("prize")
        ):
            raise ValidationError(
                "Для полезной привычки необходимо указать только связанную привычку или вознаграждение!"
            )
        elif val.get("pleasant") is True and (
            val.get("prize") or val.get("related_habit")
        ):
            raise ValidationError(
                "Для приятной привычки не может быть связанной привычки или вознаграждения!"
            )
        elif val.get("period") > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем раз в 7 дней!")
