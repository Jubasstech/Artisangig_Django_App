from django import forms
from .models import Customer, Artisan

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'address', 'profile_picture']
        
class ArtisanRegistrationForm(forms.ModelForm):
    class Meta:
        model = Artisan
        fields = ['name', 'phone_number', 'address', 'identification_document', 'account_number', 'bvn']

