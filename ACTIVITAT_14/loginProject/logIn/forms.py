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
            user = User.objects.filter(email=email).first()
            if user is None:
                raise forms.ValidationError("Este email no está registrado.")
            if not user.check_password(password):
                raise forms.ValidationError("Contraseña incorrecta.")
        return self.cleaned_data
