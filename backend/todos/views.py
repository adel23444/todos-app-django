from rest_framework import generics, serializers
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializers_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer