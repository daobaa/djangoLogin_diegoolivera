from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailAuth(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Este email no está registrado.")

        return self.cleaned_data
