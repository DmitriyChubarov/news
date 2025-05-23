import requests
from django.shortcuts import render,redirect
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny

from .serializers import NewsSerializerPOST, NewsSerializerGET, NewsSerializerPUT
from .models import News

class NewsViewPOST(generics.CreateAPIView):
    '''Вьюха для отправки POST запросов на создание новости'''
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializerPOST

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class NewsViewGET(generics.ListAPIView):
    '''Вьюха для отправки GET запросов на получение всех новостей'''
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializerGET

def NewsViewGetHTML(request):
    token = request.session.get('token')
    headers = {'Authorization': f'Token {token}'}
    response = requests.get('http://127.0.0.1:8000/news/get-news/', headers=headers)
    if response.status_code == 200:
        news = response.json()
        return render(request, 'news-board/get-news.html', {'news': news})
    print(token)
    print(response.status_code)
    return redirect('login-html')

class NewsViewPATCH(generics.RetrieveUpdateAPIView):
    '''Вьюха для отправки PATCH запросов на изменение новости'''
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializerPUT

class NewsViewDELETE(generics.RetrieveDestroyAPIView):
    '''Вьюха для отправки DELETE запросов на удаление новости'''
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializerGET

    def get_object(self):
        obj = super().get_object()
        if self.request.user.username == obj.author.username:
            return obj
        if self.request.user.is_superuser == True:
            return obj
        else:
            raise PermissionDenied("Вы не являетесь автором этого обьекта")
