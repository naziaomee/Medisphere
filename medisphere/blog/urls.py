# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog_list"),  # List of healthcare articles
    path("create/", views.blog_create, name="blog_create"),
]
