from django.shortcuts import render,get_object_or_404 
from .models import Post

def mainpage(request):
    return render(request, 'mainpage.html')

def newslist(request):
    return render(request, 'newslist.html',
            {'posts':Post.objects.all()})

def seenews(request, id2):
    post = get_object_or_404(Post, id = id2)
    return render(request, 'seenews.html',
    {'post': post})

def navigation(request):
    return render(request, 'navigation.html')