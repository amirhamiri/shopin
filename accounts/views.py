from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View
from shopin import settings
from django.utils.translation import gettext as _

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