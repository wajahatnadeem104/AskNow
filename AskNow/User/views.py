from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView
from User.form import RegistrationForm, LoginForm, ChangePasswordForm
from User.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        return render(request, 'account/login.html', {'form': login_form})

    def post(self, request):
        login_form = LoginForm(request=request, data=request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
        messages.info(request, 'Email OR Password is incorrect ')
        return render(request, 'account/login.html', {'form': login_form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('login'))


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/register.html'

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(reverse('home'))
        return super().form_valid(form)


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('home')
