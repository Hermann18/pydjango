from django.shortcuts import render,get_object_or_404 
from .models import Post, message
from .forms import MessageForm, LoginForm, UserRegistrationForm
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
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, '/mainapp/register.html', {'user_form': user_form})
