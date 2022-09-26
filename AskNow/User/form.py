from django import forms
from User.models import User
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=60, widget=forms.EmailInput(attrs={'placeholder': 'Email...', 'class': 'form-control'}))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password...'}))

    class Meta:
        fields = ('username', 'password')


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password...'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Re-enter Password...'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'UserName...', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email...', 'class': 'form-control'}),
        }


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Old Password...'}))
    new_password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'New Password...'}))
    new_password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Re-enter New Password...'}))

    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')
