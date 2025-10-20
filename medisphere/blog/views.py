# blog/views.py
from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.shortcuts import redirect


def blog_list(request):
    blogs = Blog.objects.all()  # Fetch all blog posts
    return render(request, "blog/blog_list.html", {"blogs": blogs})


def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("blog_list")
    else:
        form = BlogForm()
    return render(request, "blog/blog_create.html", {"form": form})
