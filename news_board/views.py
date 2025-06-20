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

#API
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

class NewsViewPATCH(generics.RetrieveUpdateAPIView):
    '''Вьюха для отправки PATCH запросов на изменение новости'''
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializerPUT

    def get_object(self):
        obj = super().get_object()
        if self.request.user.username == obj.author.username:
            return obj
        if self.request.user.is_superuser == True:
            return obj
        else:
            raise PermissionDenied("Вы не являетесь автором этого обьекта")

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

            return render(request, 'news-board/get-news.html', {'error': error})

#HTML
def NewsViewPostHTML(request):
    '''Вьюха для HTML страницы создания новости''' 
    if request.method == 'POST':
        token = request.session.get('token')
        headers = {'Authorization': f'Token {token}'}
        title = request.POST.get('title')
        content = request.POST.get('content')
        data = {'title': title, 'content': content}
        try:
            response = requests.post('http://127.0.0.1:8000/news/create-news/', headers=headers, data=data)
            return redirect('get-news-html')
        except Exception as error:
            return render(request, 'news-board/create_news.html', {'error': error})
    return render(request, 'news-board/create_news.html')

def NewsViewGetHTML(request):
    '''Вьюха для HTML странички со всеми новостями'''
    token = request.session.get('token')
    headers = {'Authorization': f'Token {token}'}
    response = requests.get('http://127.0.0.1:8000/news/get-news/', headers=headers)
    author = request.user.username
    if response.status_code == 200:
        news = response.json()
        return render(request, 'news-board/get-news.html', {'news': news})
    return redirect('login-html')

def NewsViewPatchHTML(request, pk):
    '''Вьюха для HTML страницы редактирования новости''' 
    if request.method == 'POST':
        token = request.session.get('token')
        headers = {'Authorization': f'Token {token}'} 
        try:
            response = requests.patch(f'http://127.0.0.1:8000/news/edit-news/{pk}/', headers=headers)
            return redirect('get-news-html')
        except Exception as error:
            return render(request, 'news-board/edit_news.html', {'error': error})
    return render(request, 'news-board/edit_news.html', {'pk': pk})

def NewsViewDeleteHTML(request, pk):
    '''Вьюха для удаления новости''' 
    if request.method == 'POST':
        token = request.session.get('token')
        headers = {'Authorization': f'Token {token}'} 
        try:
            response = requests.delete(f'http://127.0.0.1:8000/news/delete-news/{pk}/', headers=headers)
            return redirect('get-news-html')
        except Exception as error:
            return render(request, 'news-board/get-news.html', {'error': error})
