from rest_framework import serializers
from .models import News

class NewsSerializerPOST(serializers.ModelSerializer):
    '''Сериализатор для отправки POST запроса на создание новости'''
    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['author']

class NewsSerializerGET(serializers.ModelSerializer):
    '''Сериализатор для отправки GET запроса на получение всех новостей'''
    class Meta:
        model = News
        fields = '__all__'

