from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class ToDo(models.Model):
    '''модель задачи'''

    headline = models.CharField(
        max_length=100, blank=False, verbose_name='Заголовок',)
    description = models.TextField(blank=False, verbose_name='Описание',)
    deadline = models.DateTimeField(blank=True, null=True, default=None, verbose_name='Дата сдачи',)
    execute = models.BooleanField(default=False, verbose_name='Отметка',)

    def clean(self):
        if self.deadline != None:
            if self.deadline < timezone.now():
                raise ValidationError("The date cannot be in the past!")

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        '''Строковое отображение'''
        return f'{self.headline}'
