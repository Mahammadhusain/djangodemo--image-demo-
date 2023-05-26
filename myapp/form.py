# --------- Form.py ---------
from django import forms
from django.contrib.auth.forms import (UserCreationForm,AuthenticationForm,
UserChangeForm,PasswordResetForm,SetPasswordForm,PasswordChangeForm)
from django.contrib.auth.models import User


# User Signin
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','password']