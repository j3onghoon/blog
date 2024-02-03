from datetime import timedelta

from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework import serializers, viewsets

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter().prefetch_related("category")
    serializer_class = PostSerializer


def review_all(request):
    if 'HX-Request' not in request.headers:
        return redirect('/')
    posts = Post.objects.all()
    return render(request, 'blog/review/all.html', {'posts': posts})


def review_some(request):
    if 'HX-Request' not in request.headers:
        return redirect('/')
    RETENTION_CURVES = [1, 3, 6, 30, 90, 180]
    retention_curve = Q()
    for curve in RETENTION_CURVES:
        retention_curve |= Q(updated__date=timezone.localdate() - timedelta(days=curve))
    posts = Post.objects.filter(retention_curve)
    return render(request, 'blog/review/some.html', {'posts': posts})


def review(request):
    RETENTION_CURVES = [1, 3, 6, 30, 90, 180]
    retention_curve = Q()
    for curve in RETENTION_CURVES:
        retention_curve |= Q(updated__date=timezone.localdate() - timedelta(days=curve))
    posts = Post.objects.filter(retention_curve)
    return render(request, 'blog/review/index.html', {'posts': posts})
