from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import makeEvent

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class eventMakerForm(forms.ModelForm):
    
    class Meta:
        model = makeEvent
        fields = ("event_name","event_date","event_desc","event_contact","event_poster")