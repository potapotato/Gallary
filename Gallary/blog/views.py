from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.


def blog(request):
    blogs = models.Blog.objects
    print(blogs.all)
    return render(request, 'blog.html', {'blogs': blogs})

def blog_text(request, blog_id):
    blog = get_object_or_404(models.Blog, pk=blog_id)
    return render(request, 'blog_text.html', {'blog':blog})
# todo: 省略号