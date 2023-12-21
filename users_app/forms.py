from django import forms


class RegisterForm(forms.Form):
    names = forms.CharField(max_length=120)
    phone = forms.CharField(max_length=15)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)