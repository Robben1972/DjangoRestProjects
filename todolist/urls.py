from django.urls import path, include
from .views import TodoListView, todo_detail

urlpatterns = [
    path('', TodoListView.as_view()),
    path('<int:pk>/', todo_detail)
]
