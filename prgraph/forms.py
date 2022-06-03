
from django import forms
from .models import Category

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('id','name')
