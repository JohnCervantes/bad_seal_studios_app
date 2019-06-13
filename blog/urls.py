from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_blogs, name='blog_blogs'),
    path('about/', views.about, name='blog_about'),
    path('<int:blog_id>/', views.detail, name = 'blog_details')
]