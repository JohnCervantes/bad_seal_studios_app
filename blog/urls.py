from . import views
from django.urls import path
from .views import PostListViews, PostDetailViews, PostCreateViews, PostUpdateViews, PostDeleteViews

urlpatterns = [
    path('', PostListViews.as_view(), name='blog_blogs'),
    path('about/', views.about, name='blog_about'),
    path('post/<int:pk>/', PostDetailViews.as_view() , name = 'blog_details'),
    path('post/new/', PostCreateViews.as_view() , name = 'blog_create'),
    path('post/<int:pk>/update', PostUpdateViews.as_view() , name = 'blog_update'),
    path('post/<int:pk>/delete', PostDeleteViews.as_view() , name = 'blog_delete'),

]