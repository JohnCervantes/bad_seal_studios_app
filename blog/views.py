from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)  # pk is primary key
    return render(request, 'blog/details.html', {'blog': detail_blog, 'title': Blog.title})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class PostListViews(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    # blogs will be the name containing all of the iterable objects
    context_object_name = 'blogs'
    # ascending is ['date_posted'] . descending is ['-date_posted']
    ordering = ['-pub_date']
    paginate_by = 5



class PostDetailViews(DetailView):
    model = Blog
    template_name = 'blog/details.html'
    


class PostCreateViews(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateViews(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'body']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteViews(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        
