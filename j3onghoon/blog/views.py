from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category


def index(request):
    latest_post_list = Post.objects.order_by("-created")[:5]
    context = {
        "latest_post_list": latest_post_list,
    }
    return render(request, "blog/index.html", context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/detail.html", {"post": post})


def new(request):
    return render(request, "blog/new.html")


def post(request):
    category = Category.objects.filter(id=request.POST.get("category")).first()
    Post.objects.create정(title=request.POST.get("title"), content=request.POST.get("content"), category=category)
    return redirect('blog:index')


def review(request):
    pass
    return render(request, "blog/reveiw.html", context)