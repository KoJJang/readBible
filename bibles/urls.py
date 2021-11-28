from django.urls import path
from . import views

urlpatterns = [
    path('', views.bible_list, name='bible_list'),
    path('bible/<int:pk>/', views.bible_detail, name='bible_detail'),
    path('bible/new/', views.bible_new, name='bible_new'),
    path('bible/<int:pk>/edit/', views.bible_edit, name='bible_edit')
]