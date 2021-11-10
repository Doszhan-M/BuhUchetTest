from django.contrib import admin

from .models import ToDo 


class ToDoPanel(admin.ModelAdmin):
    list_display = ('id', 'headline', 'deadline', 'execute',)
    list_display_links = ('headline', 'deadline', 'execute',)
    ordering = ['-id']

admin.site.register(ToDo, ToDoPanel)