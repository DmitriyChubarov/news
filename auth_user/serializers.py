from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from .func import create_user_in_serializer

User = get_user_model()

class Registerserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        return create_user_in_serializer(username, password)

class Loginserializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('invalid auth')
        data['user'] = user
        return data
