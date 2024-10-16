from rest_framework.serializers import ValidationError

from course_work_DRF.habits.models import Habit


class HabitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value)
        if val.get('complete_time') > 2:
            raise ValidationError('Время выполнения должно быть не более 2 минут!')
        elif val.get('pleasant') is False and (val.get('related_habit') and val.get('prize')):
            raise ValidationError('Для полезной привычки необходимо указать только связанную привычку или вознаграждение!')
        elif value['pleasant'] is True and (value['prize'] or value['related_habit']):
            raise ValidationError('Для приятной привычки не может быть связанной привычки или вознаграждения!')
        elif value['period'] > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем раз в 7 дней!')
        # elif val['related_habit'] is not None:
        #     rel_hab = val['related_habit']
        #     if rel_hab['pleasant'] is False:
        #         raise ValidationError('Связанной привычкой может быть только приятная привычка!')

def validate_related_habit(value):
    habit = Habit.objects.all()
    if item not in value:
        raise ValidationError(f'Ссылка не корректна. Используйте материалы с {item}.')