from django.forms import ModelForm, TextInput, Textarea
from .models import message

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