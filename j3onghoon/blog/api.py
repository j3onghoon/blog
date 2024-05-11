# from django.core.paginator import Paginator
from datetime import timedelta, datetime
import markdown

from django.db.models import Q
from django.shortcuts import render, redirect
from rest_framework import serializers, viewsets

from .models import Post, Work, WorkDetail, WorkKeyWord, KeyWord, Career


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


def resume(request):
    career_infos = []
    for career in Career.objects.order_by('-start_date'):
        career_info = {'career': career, 'work_infos': []}
        for work in Work.objects.filter(career=career):
            career_info['work_infos'].append({'work': work, 'work_detail': WorkDetail.objects.filter(work=work),
                                              'work_keyword': KeyWord.objects.filter(
                                                  id__in=WorkKeyWord.objects.filter(work=work).values_list('keyword',
                                                                                                           flat=True))})

        career_infos.append(career_info)

    return render(request, 'blog/resume.html', {
        'career_infos': career_infos
    })
