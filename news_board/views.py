from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import NewsSerializer
from rest_framework.permissions import IsAuthenticated
from .models import News

class NewsView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
