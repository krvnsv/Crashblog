from operator import pos
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE) # get filtered posts from database

    return render(request, 'core/frontpage.html', {'posts': posts}) # dictionary makes posts available on the front end

def about(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")