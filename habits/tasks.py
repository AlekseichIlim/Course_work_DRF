from celery import shared_task

from habits.services import send_telegram_massage
from datetime import datetime, timedelta

from config import settings
from habits.models import Habit
@shared_task()
def telegram_messages():
    time_now = datetime.now()
    habits = Habit.objects.all()

    for habit in habits:

        user_tg_id = habit.owner.tg_chat_id
        if habit.time_action:
            if user_tg_id and time_now >= habit.time_action - timedelta(minutes=20):
                if habit.pleasant:
                    message = f"{habit.action} в {habit.time_action}'! Продолжайте её выполнять!"
                else:
                    message = f"{habit.action} в {habit.time_action}'! Не забывайте о вознаграждении: {habit.prize}{habit.related_habit}!"

                telegram_messages(user_tg_id, message)
        else:
            message = f"{habit.action} в {habit.time_action}'! Не забывайте о вознаграждении: {habit.prize}{habit.related_habit}!"
            telegram_messages(user_tg_id, message)
