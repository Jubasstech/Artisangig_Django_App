"""
URL configuration for ArtisanGig project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    path('', include('core.urls')),
path('', core_views.home, name='home'),
    path('customer/register/', core_views.customer_registration, name='customer_registration'),
    path('artisan/register/', core_views.artisan_registration, name='artisan_registration'),
    path('artisan/dashboard/', core_views.artisan_dashboard, name='artisan_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # Add other app URLs here if needed
]

INSTALLED_APPS = [
    # ...
    'paystack',
    # ...
]

PAYSTACK_PUBLIC_KEY = 'YOUR_PUBLIC_KEY'
PAYSTACK_SECRET_KEY = 'YOUR_SECRET_KEY'
PAYSTACK_SUCCESS_URL = '/payment/success/'
PAYSTACK_FAILED_URL = '/payment/failed/'

urlpatterns = [
    path('admin/', admin.site.urls),
]
