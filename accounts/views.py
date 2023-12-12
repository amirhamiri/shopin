from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.translation import gettext as _
from shopin import settings
from .forms import RegisterForm
from .models import User


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "accounts/register_form.html", context={"form": form})


    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(phone=phone, password=password)
            messages.success(request, _("Register successful."))
            return redirect('accounts:register')
        else:
            return render(request, "accounts/register_form.html", context={"form": form})

class LoginView(View):
    def get(self, request):
        return render(request, "accounts/login_form.html")

    def post(self, request):
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, _("Login successful."))
            return redirect('accounts:login')
        else:
            messages.error(request, _("Invalid phone or password."))
            return redirect('accounts:login')

        return render(request, "index.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)