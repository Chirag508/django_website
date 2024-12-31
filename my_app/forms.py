from django import forms
from .models import product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ('name','details','price','quantity')

class userreggistarationform(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']