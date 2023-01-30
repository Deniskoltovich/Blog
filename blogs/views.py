from django.shortcuts import render, get_object_or_404
from .models import Blog
from posts.models import Post


def list_blogs(request):
    blogs = Blog.objects.all()
    ctx = {
        'title': 'Blogs',
        'blogs': blogs
    }
    return render(request, 'list_blogs.html', ctx)


def show_blog(request, id: int):
    blog = get_object_or_404(Blog, pk=id)
    posts = Post.objects.filter(blog__pk=id)
    ctx = {
        'title': blog.title,
        'blog': blog,
        'posts': posts
    }
    return render(request, 'show_blog.html', ctx)