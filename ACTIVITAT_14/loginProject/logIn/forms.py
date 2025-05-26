from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailAuth(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)