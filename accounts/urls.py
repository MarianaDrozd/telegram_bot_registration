"""telegram_registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from accounts.views import HomeView, RegisterView, AccountView, save_user

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('account/<int:pk>/', AccountView.as_view(), name='account'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('register/', RegisterView.as_view(), name='register'),
    path('save-user/', save_user, name='save_new_user'),

]
