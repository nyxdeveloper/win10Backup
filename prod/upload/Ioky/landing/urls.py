from django.urls import path, include
from landing import views

urlpatterns = [
    path('', views.HomePageRu.as_view()),
    path('create-question/', views.CreateQuestion.as_view(), name='create-question'),
    path('ru/', views.HomePageRu.as_view(), name='ru'),
    path('en/', views.HomePageEn.as_view(), name='en'),
]