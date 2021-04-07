from django.forms import ModelForm, TextInput, Textarea
from .models import message
from django.contrib.auth.models import User
from django import forms

class MessageForm(ModelForm):
    class Meta:
        model = message
        fields = ['text','author']
        widgets = {
             'author':TextInput(attrs = {
                'class':'form-author',
                'placeholder':'Анонимус'
            }),
            'text':Textarea( attrs = {
                'class':'form-text',
                'placeholder':'>пук'
            } )
        }
        #help_texts = { 'author': 'АНОНИМУС', 'text':'>пук'} 
        #labels = {'text': "текст", 'author':'Автор'}

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'NoNigger1488'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'placeholder': 'NoNigger1488'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
             'username':TextInput(attrs = {
                'class':'form-username',
                'placeholder':'AverageFemboyLover',
                }),
            
            'email':TextInput( attrs = {
                 'class':'form-email',
                 'placeholder':'adolf.hitler.228@gmail.com'
             }),
        }
        labels = {'username':'Nickname', 'email':'Email'}
        help_texts = {'username': "Unique identifier for you and place to your fanatasy",}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ['username','password']
        labels = {'username':'Nickname'}
        help_texts = {'username': "",}
    
    def clean(self):
        cd = self.cleaned_data
        if not User.objects.filter(username = cd['username']).exists():
            raise forms.ValidationError('User doesn\'t exist')
        user = User.objects.filter(username = cd['username']).first()
        if user:
            if not user.check_password(cd['password']):
                raise forms.ValidationError('Password invalid')
        return self.cleaned_data
