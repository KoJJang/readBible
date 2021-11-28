from django.urls import path
from . import views

urlpatterns = [
    path('', views.bible_list, name='bible_list'),
    path('bible/<int:pk>/', views.bible_detail, name='bible_detail'),
]