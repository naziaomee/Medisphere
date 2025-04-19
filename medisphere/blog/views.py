# blog/views.py
from django.shortcuts import render
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()  # Fetch all blog posts
    return render(request, 'blog/blog_list.html', {'blogs': blogs})