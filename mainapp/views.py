from django.shortcuts import render,get_object_or_404 
from .models import Post, message
from .forms import MessageForm
from django.shortcuts import redirect

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

def livechat(request):
    form = MessageForm()
    return render(request, 'livechat.html',
    {'mess':reversed(message.objects.all()), 'form':form })

def sendmessage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/mainapp/livechat/')
