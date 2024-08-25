from django.urls import path
from .views import ProfileMakerViews, profile_maker_detail

urlpatterns = [
    path('', ProfileMakerViews.as_view()),
    path('<int:pk>/', profile_maker_detail),
]
