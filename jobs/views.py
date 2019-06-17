from django.shortcuts import render
from .models import Projects
from django.views.generic import ListView, DetailView


class PostListViews(ListView):
    model = Projects
    template_name = 'jobs/home.html'
    # blogs will be the name containing all of the iterable objects
    context_object_name = 'projects'
    # ascending is ['date_posted'] . descending is ['-date_posted']
    ordering = ['-date_posted']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(PostListViews,self).get_context_data(**kwargs)
        context['title'] = 'Projects'
        context['count'] = self.model.objects.all().count()
        context['complete'] = self.model.objects.filter(status='Complete').count()
        context['in_progress'] = self.model.objects.filter(status='In Progress').count()
        return context

class PostDetailViews(DetailView):
    model = Projects
    template_name = 'jobs/project_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Projects.objects.get(id=self.kwargs['pk']).title
        return context
