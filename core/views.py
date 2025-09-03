from operator import pos
from django.shortcuts import render

from blog.models import Post

def frontpage(request):
    posts = Post.objects.all() # get all posts from database

    return render(request, 'core/frontpage.html', {'posts': posts}) # dictionary makes posts available on the front end

def about(request):
    return render(request, 'core/about.html')