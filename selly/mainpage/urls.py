from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainpageView.as_view(), name='mainpage')
]