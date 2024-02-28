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


def create_post(request):
    category = Category.objects.filter(id=request.POST.get("category")).first()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    Post.objects.create(title=request.POST.get("title"), content=f'{request.POST.get("new-post")}\n{ip}', category=category)
    return redirect('blog:index')


def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    category = Category.objects.filter(id=request.POST.get("category")).first()
    title = request.POST.get("title")
    content = request.POST.get("update-post")

    post.title = title
    post.content = content
    post.category = category
    post.save()
    return redirect('blog:index')
