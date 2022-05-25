from django import forms

class NameForm(forms.Form):
    your_name = forms.EmailField(label='Your name', max_length=100)