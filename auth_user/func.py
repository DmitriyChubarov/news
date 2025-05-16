from .models import User

def create_user_in_serializer(username, password):
    '''Создание пользователя в БД'''
    user = User.objects.create_user(username=username, password=password)
    return user
