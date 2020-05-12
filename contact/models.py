from django.db import models


class Contacts(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email