from django.db import models

# class Exercise(models.Model):
#     title = models.CharField('Название упражнения', max_length=30)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Упражнение'
#         verbose_name_plural = 'Упражнения'

class Train(models.Model):
    title = models.CharField('Название тренировки', max_length=50, default='Новая тренировка')
    comment = models.CharField('Комментарий', max_length=250, null=True, blank=True)
    exercises = models.CharField('Упражнения', max_length=300)
    data = models.DateTimeField('Дата тренировки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'
