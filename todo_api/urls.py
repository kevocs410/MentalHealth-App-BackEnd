from django.urls import path
from .import views

urlpatterns = [
    path('api/todos', views.TodoList.as_view(), name='todo_list'),
    path('api/todos/<int:pk>', views.TodoDetail.as_view(), name='todo_detail'),
]