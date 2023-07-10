from django.db import models

# Create your models here.
from django.db import models
from django.db import models

class Customer(models.Model):
    # Define customer fields (e.g., name, contact details, etc.)

class Artisan(models.Model):
    # Define artisan fields (e.g., name, contact details, portfolio, etc.)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    # Define order fields (e.g., order details, status, payment details, etc.)

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):                         user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)                                                      class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    bvn = models.CharField(max_length=11)
    id_proof = models.ImageField(upload_to='id_proofs')

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2)

from django.db import models

class Work(models.Model):
    CATEGORY_CHOICES = (
        ('Category 1', 'Category 1'),
        ('Category 2', 'Category 2'),
        ('Category 3', 'Category 3'),
        # Add more category choices as needed
    )

    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='artisans_works/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
class Work(models.Model):
    # ...
    paid = models.BooleanField(default=False)


