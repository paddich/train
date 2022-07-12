from django.db import models

# class Training(models.Model):
#     title = # название тренировки, проверка на существующее, не обязательное поле
#     # muscle = # определяется автоматически на основе выбранных упражнений и пока не нужно
#     exercise = # добавить существующее упражнение из списка
#     date = models.DateField(auto_now=True)
#
# class ExerciseEdit(models.Model):
#     title = models.CharField(max_length=50) # название упражнения, проверка на существующее, обязательное поле
#     # muscle = # пока не нужно, не обязательное поле
#
# class ExerciseWrite(models.Model):
    # title =  уже созданное упражнение из списка
    # weight =
    # rep =
    # approach = устанавливается по количеству пар wight + rep
    # date = models.DateField(auto_now=True)