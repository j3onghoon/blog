from django.urls import path

from . import views
from .api import post_all, post_list

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('new', views.new, name="new"),
    path('create_post', views.create_post, name='create_post'),
    path('post_list', post_list, name="post_list"),
    path('post_all', post_all, name="post_all")
]
