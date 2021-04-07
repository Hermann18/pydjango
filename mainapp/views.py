from django.shortcuts import render,get_object_or_404 
from .models import Post, message
#from django import forms
from .forms import MessageForm, UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, logout as dj_logout, login as dj_login
#LoginForm,
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

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            usser = authenticate(username = user_form.cleaned_data['username'], password = user_form.cleaned_data['password'])
            dj_login(request, usser)
            return render(request, 'register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login(request):
    if request.method == 'POST':
        user = LoginForm(request.POST)
        if user.is_valid():  
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']
            usser = authenticate(username = username, password = password)
            if usser:
                dj_login(request, usser)
                return render(request, 'register_done.html')
    else:
        user = LoginForm()
    return render(request, 'login.html', {'user_form': user})     

def logout(request):
    dj_logout(request)  
    return render(request, 'register_done.html')

    
