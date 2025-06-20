import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from .serializers import Registerserializer, Loginserializer
from rest_framework.permissions import AllowAny

#API
class RegisterView(APIView):
    '''Вьюха регистрации пользователя'''
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = Registerserializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'user create'}, status=200)
        return Response({'message': 'error'}, status=404)

class LoginView(APIView):
    '''Вьюха авторизации пользователя, создание/проверка и возврат токена'''
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = Loginserializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        return Response({'message': 'invalid auth'}, status=400)

#HTML
def MainViewHTMl(request):
    '''Вьюха для главное страницы входа'''
    return render(request, 'auth/main.html')

def RegisterViewHTML(request):
    '''Вьюха для создания страницы регистрации'''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        data = {
            'username': username,
            'password': password
        }
    
        response = requests.post('http://127.0.0.1:8000/register/', data=data)
        if response.status_code == 200:
            return redirect('login-html')
        else:
            return render(request, 'auth/register.html', {'error': 'Ошибка регистрации'})
    return render(request, 'auth/register.html')

def LoginViewHTML(request):
    '''Вьюха для создания страницы авторизации'''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        data = {
            'username': username,
            'password': password
        }
    
        response = requests.post('http://127.0.0.1:8000/login/', data=data)
        if response.status_code == 200:
            token = response.json().get('token')
            request.session['token'] = token

        user = authenticate(request, username=username, password=password)
        if user :
            login(request, user)
            return redirect('main-auth-html')
        else:
            return render(request, 'auth/login.html', {'error': 'Ошибка авторизации'})
    return render(request, 'auth/login.html')
