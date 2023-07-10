# payment_signal.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import Order, Payment

User = get_user_model()

@receiver(post_save, sender=Payment)
def process_payment(sender, instance, created, **kwargs):
    if created:
        # Update the order status
        order = instance.order
        order.status = 'paid'
        order.save()
        
        # Perform any additional tasks after payment is processed
        # e.g., send email notifications, update inventory, etc.
        # ...
        
        # Disburse payment to the artisan
        artisan = order.artisan
        artisan.balance += instance.amount
        artisan.save()
        
        # Disburse payment to the app owner
        app_owner = User.objects.get(username=settings.APP_OWNER_USERNAME)
        app_owner.balance += instance.amount
        app_owner.save()

