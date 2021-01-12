from django.urls import path
from . import views

urlpatterns = [
    path('1', views.ex1, name="ex1"),
    path('2', views.ex2, name="ex2")
]