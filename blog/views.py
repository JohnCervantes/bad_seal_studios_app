from django.shortcuts import render
from .models import Blog

# Create your views here.
def show_blogs(request):
    blogs = Blog.objects
    return render(request, 'blog/blog.html', {'blogs':blogs})
