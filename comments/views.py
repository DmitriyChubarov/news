from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import  generics
from .serializers import CommentSerializerCreate
from .models import Comment

#API
class CommentsViewCreate(generics.CreateAPIView):
    '''Вьюха для отправки POST запросов на создание новости'''
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerCreate

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentsViewDelete(generics.RetrieveDestroyAPIView):
    '''Вьюха для отправки DELETE запроса на создание новости'''
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerCreate

