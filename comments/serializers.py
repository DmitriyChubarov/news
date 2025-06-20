from rest_framework import serializers
from .models import Comment

class CommentSerializerCreate(serializers.ModelSerializer):
    '''Сериализатор для отправки POST запроса на создание комментариев'''
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author']
