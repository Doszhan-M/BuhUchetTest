from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import ToDo
from .tasks import execution_change_alert


@receiver(pre_save, sender=ToDo)
def execution_change(sender, instance, **kwargs):
    '''Создать уведомление на почту если изменен execute.
    '''
    if instance.id is None:  # создается новый объект
        pass
    else:
        previous = ToDo.objects.get(id=instance.id)
        if previous.execute != instance.execute:  # старое значение не равно новому
            execution_change_alert.delay(instance.headline, instance.execute)
