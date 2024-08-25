from django.urls import path
from .views import CommentList, BlogList, BlogDetail, CommentDetail

urlpatterns = [
    path('', BlogList.as_view()),
    path('<int:pk>/', BlogDetail.as_view()),
    path('<int:pk>/comments/', CommentList.as_view()),
    path('<int:pk>/comments/<int:pk>/', CommentDetail.as_view()),
]
