from rest_framework import serializers

from habits.validators import HabitsValidator

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [HabitsValidator(fields)]


# class SubscriptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subscription
#         fields = '__all__'
#
#
# class CourseSerializer(serializers.ModelSerializer):
#     count_lessons = serializers.SerializerMethodField(read_only=True)
#     lesson = LessonSerializer(many=True, read_only=True)
#     subscription = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = Course
#         fields = "__all__"
#
#     #         поля которые будут в ответе Postman
#
#     def get_count_lessons(self, instance):
#
#         return instance.lesson.all().count()
#
#     def get_subscription(self, obj):
#         user = self.context['request'].user
#         if Subscription.objects.filter(user=user, course=obj).exists():
#             return "Оформлена подписка"
#         return "Не оформлена подписка"
