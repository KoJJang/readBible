from django.urls import path

from . import views

app_name = 'qnadash'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question_create/', views.question_create, name='question_create'),
]