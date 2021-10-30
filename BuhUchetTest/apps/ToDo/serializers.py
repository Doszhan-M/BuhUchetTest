from rest_framework import serializers
from django.utils import timezone

from .models import ToDo


class ToDoListserializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)  # только на чтение.
    execute = serializers.BooleanField(read_only=True)  # только на чтение.

    class Meta:
        model = ToDo
        fields = ('id', 'headline', 'description', 'deadline', 'execute',)


class ToDoserializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)  # только на чтение.

    class Meta:
        model = ToDo
        fields = ('id', 'headline', 'description', 'deadline', 'execute',)

    def validate(self, data):
        try:
            if data['deadline'] < timezone.now():
                raise serializers.ValidationError(
                    "Дедлайн не может быть в прошлом")
        except KeyError:
            pass
        return data
