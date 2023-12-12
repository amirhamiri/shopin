from django.urls import path
from accounts import views


app_name = 'accounts'
urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register')
]
