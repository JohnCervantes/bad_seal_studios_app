from . import views
from django.urls import path
from .views import PostListViews, PostDetailViews

urlpatterns = [
    path('', PostListViews.as_view(), name = 'projects'),
    path('<int:pk>', PostDetailViews.as_view(), name = 'project_details')

]