from django.shortcuts import render, redirect
from .models import Post


def show_feed(request):
    posts = Post.objects.all()
    ctx = {
        'title': 'Feed',
        'posts': posts,
    }
    return render(request, 'feed.html', ctx)


def create_post(request): ...


def redirect_to_blog(request, id: int):
    return redirect(f'/blogs/{id}/')
