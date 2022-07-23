from django.db import models

class Client(models.Model):
    name = models.CharField('имя', max_length=50)
    name2 = models.CharField('фамилия', max_length=50)
    name3 = models.CharField('отчество', max_length=50)
    fullname = [name, name2, name3]
    age = models.CharField('возраст', max_length=3)
    date = models.DateTimeField('дата создания карточки')

    # def __str__(self):
    #     return self.fullname
    #
    # def get_absolute_url(self):
    #     return f'/news/{self.id}'
    #
    # class Meta:
    #     verbose_name = 'Клиенты'
    #     verbose_name_plural = 'Клиенты'

class Training(models.Model):
    client_action = models.ForeignKey(Client, on_delete=models.CASCADE())
