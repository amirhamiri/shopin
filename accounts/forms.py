from django.forms import ModelForm, forms

from accounts.models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'password']