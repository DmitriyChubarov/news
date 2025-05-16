from django.db import models
from django.contrib.auth.models import AbstractUser
from auth_user.models import User

class News(models.Model):
    '''Модель новости'''
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User,
                        on_delete=models.CASCADE,
                        null=False)

    class Meta():
        db_table='news'

    def __str__(self):
        return self.title
