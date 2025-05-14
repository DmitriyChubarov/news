from .models import User

def create_user_in_serializer(username, password):
    user = User.objects.create_user(username=username, password=password)
    return user
