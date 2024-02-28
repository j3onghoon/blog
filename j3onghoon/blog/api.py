# from django.core.paginator import Paginator
from datetime import timedelta, datetime
import markdown

from django.db.models import Q
from django.shortcuts import render, redirect
from rest_framework import serializers, viewsets

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter().prefetch_related("category")
    serializer_class = PostSerializer


def post_all(request):
    if 'HX-Request' not in request.headers:
        return redirect('/')
    posts = Post.objects.all().order_by('-created')
    for post in posts:
        post.content = markdown.markdown(post.content, extensions=['fenced_code', 'tables'])
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_list(request):
    RETENTION_CURVES = [1, 3, 6, 30, 90, 180]
    retention_curve = Q()
    for curve in RETENTION_CURVES:
        retention_curve |= Q(updated__date=datetime.now() - timedelta(days=curve))
    posts = Post.objects.filter(retention_curve)
    template = 'blog/post/list.html' if request.headers.get('HX-Request') else 'blog/post/index.html'
    return render(request, template, {'posts': posts})
