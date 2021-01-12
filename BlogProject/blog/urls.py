from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"),
    path('new', views.write, name="write"),
    path('craete', views.create, name="create"),
]