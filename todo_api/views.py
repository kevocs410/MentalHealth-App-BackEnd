from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer

class TodoDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer