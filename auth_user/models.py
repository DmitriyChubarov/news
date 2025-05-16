from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''Модель пользователя'''
   # first_name = None
   # last_name = None
   # email = None
   # groups = None
   # user_permissions = None
   # is_active = None
   # is_staff = None
   # last_login = None
   # date_joined = None

    class Meta:
        db_table = 'all_users'

    def __str__(self):
        return self.username
