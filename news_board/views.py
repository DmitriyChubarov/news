from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import NewsSerializerPOST, NewsSerializerGET
from rest_framework.permissions import IsAuthenticated
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
