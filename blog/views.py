from django.shortcuts import render, get_object_or_404
from .models import Blog



def show_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blogs})


def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)  # pk is primary key
    return render(request, 'blog/details.html', {'blog': detail_blog})


def about(request):
    return render(request, 'blog/about.html', {'title':'About Page'})
