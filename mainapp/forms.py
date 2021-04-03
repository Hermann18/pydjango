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
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
             'username':TextInput(attrs = {
                'class':'form-username',
                'placeholder':'AverageFemboyLover',

            }),
            
            # 'text':Textarea( attrs = {
            #     'class':'form-text',
            #     'placeholder':'first_name'
            #     'placeholder': ''
            # } )
        }
        labels = {'username':'Nickname'}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']