from django.urls import path

from . import views
from .api import review_all, review, review_some

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('new', views.new, name="new"),
    path('post', views.post, name='post'),
    path('review/', review, name="review"),
    path('review/some', review_some, name="review_some"),
    path('review/all', review_all, name="review_all")
]
