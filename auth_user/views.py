from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from .serializers import Registerserializer, Loginserializer

class RegisterView(APIView):
    '''Вьюха регистрации пользователя'''
    def post(self, request):
        serializer = Registerserializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'user create'}, status=200)
        return Response({'message': 'error'}, status=404)

class LoginView(APIView):
    '''Вьюха авторизации пользователя, создание/проверка и возврат токена'''
    def post(self,request):
        serializer = Loginserializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        return Response({'message': 'invalid auth'}, status=400)
