from django.db import models

# Create your models here.

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=50, null=True, blank=True, choices=status_choices, default='new', verbose_name='Status')
    date = models.DateField(null=False, blank=False, verbose_name='Дата')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)
