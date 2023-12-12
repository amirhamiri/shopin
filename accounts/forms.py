from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import gettext_lazy as _
from accounts.models import User


class RegisterForm(forms.ModelForm):
    re_password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "input-ui pr-2", "type": "password", "placeholder": _("Repeat your password")}))

    class Meta:
        model = User
        fields = ['phone', 'password', 're_password']
        widgets = {
            "phone": forms.TextInput(
                attrs={"class": "input-ui pr-2", "type": "text", "placeholder": _("Enter your phone number")}),
            "password": forms.PasswordInput(
                attrs={"class": "input-ui pr-2", "type": "password", "placeholder": _("Enter your password")}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password and password != re_password:
            raise ValidationError(_("Passwords don't match"))

        return cleaned_data

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise ValidationError(_("Phone number already exists"))
        return phone

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError(_("Password must be at least 8 characters"))
        return password
