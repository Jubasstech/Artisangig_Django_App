from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('artisan/registration/', views.artisan_registration, name='artisan_registration'),
    path('customer/registration/', views.customer_registration, name='customer_registration'),
   
    path('artisan/dashboard/', views.artisan_dashboard, name='artisan_dashboard'),
    path('browse/works/', views.browse_works, name='browse_works'),
    path('chat/artisan/<int:artisan_id>/', views.chat_with_artisan, name='chat_with_artisan'),
# ...
    path('work/payment/<int:work_id>/', views.initiate_payment, name='initiate_payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/failed/', views.payment_failed, name='payment_failed'),
    # ...

    # Add other URL patterns for customer profiles, artisan profiles, etc.
]

