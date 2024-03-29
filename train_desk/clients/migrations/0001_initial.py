# Generated by Django 4.0.6 on 2022-07-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Новая тренировка', max_length=50, verbose_name='Название тренировки')),
                ('comment', models.CharField(max_length=250, verbose_name='Комментарий')),
                ('exercises', models.TextField(verbose_name='Тренировка')),
                ('data', models.DateTimeField(verbose_name='Дата тренировки')),
            ],
        ),
    ]
