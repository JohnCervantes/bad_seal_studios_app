from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from bs4 import BeautifulSoup
import requests



def about(request):
    source = requests.get('https://leetcode.com/vocalists/').text
    soup = BeautifulSoup(source, 'lxml')
    match = []
    for x in soup.find_all("span", {"class": "badge progress-bar-success"}):
        match.append(x.text)
    values = match[1].split()
    progress = str( (int(values[0]) / int(values[-1])) * 100 )


    source = requests.get('https://www.hackerrank.com/JohnCervantes?hr_r=1').text
    soup = BeautifulSoup(source, 'lxml')
    match2 = []
    for x in soup.find_all("div", {"class": "badges-wrap"}):
        match2.append(x)
    values2 = str(match2[0])

    context = {
        'values': values2,
        'leet': match[1],
        'progress':  progress,
        'latest_news': Blog.objects.all().order_by('-pub_date').values('title', 'id')[0:3],
        'title':'About'
    }
    
    return render(request, 'blog/about.html', context)


class PostListViews(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    # blogs will be the name containing all of the iterable objects
    context_object_name = 'blogs'
    # ascending is ['date_posted'] . descending is ['-date_posted']
    ordering = ['-pub_date']
    paginate_by = 5
    source = requests.get('https://leetcode.com/vocalists/').text
    soup = BeautifulSoup(source, 'lxml')
    match = []
    for x in soup.find_all("span", {"class": "badge progress-bar-success"}):
        match.append(x.text)
    values = match[1].split()
    progress = str( (int(values[0]) / int(values[-1])) * 100 )

    source = requests.get('https://www.hackerrank.com/JohnCervantes?hr_r=1').text
    soup = BeautifulSoup(source, 'lxml')
    match2 = []
    for x in soup.find_all("div", {"class": "badges-wrap"}):
        match2.append(x)
    values = str(match2[0])
  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['latest_news'] = self.model.objects.all().order_by(
            '-pub_date').values('title', 'id')[0:3]
        context['leet'] = self.match[1]
        context['progress'] = self.progress
        context['values'] = self.values
        return context


class PostDetailViews(DetailView):
    model = Blog
    template_name = 'blog/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Blog.objects.get(id=self.kwargs['pk']).title
        context['latest_news'] = self.model.objects.all().order_by(
            '-pub_date').values('title', 'id')[0:3]
        return context


class PostCreateViews(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create a Post'
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update a Post'
        return context


class PostDeleteViews(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete a Post'
        return context
