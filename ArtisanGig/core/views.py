# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect,     get_object_or_404
from django.contrib.auth.decorators import log    in_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_    exempt
from paystack.signals import payment_verified
from .forms import CustomerRegistrationFor, ArtisanRegistrationForm, WorkForm

def home(request):
    # Logic for rendering the homepage template
    return render(request, 'home.html')
   from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm, ArtisanRegistrationForm

def artisan_registration(request):
    if request.method == 'POST':
        form = ArtisanRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Handle successful registration (e.g., redirect to dashboard)
            return redirect('artisan_dashboard')
    else:
        form = ArtisanRegistrationForm()
    return render(request, 'artisan_registration.html', {'form': form})

def customer_registration(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Handle successful registration (e.g., redirect to customer profile)
            return redirect('customer_profile')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customer_registration.html', {'form': form})

# Define other views for customer profiles, artisan profiles, etc.


@login_required
def artisan_dashboard(request):
    artisan = Artisan.objects.get(pk=request.user.id)
    
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.artisan = artisan
            work.save()
            # Handle successful work upload (e.g., redirect to dashboard or show success message)
            return redirect('artisan_dashboard')
    else:
        form = WorkForm()
    return render(request, 'artisan_dashboard.html', {'form': form})

def browse_works(request):
    works = Work.objects.all()
    return render(request, 'browse_works.html', {'works': works})

@login_required
def initiate_payment(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    return render(request, 'payment.html', {'work': work})

@login_required
def payment_success(request):
    # Handle successful payment (e.g., mark work as paid)
    work_id = request.session.get('work_id')
    work = get_object_or_404(Work, pk=work_id)
    work.paid = True
    work.save()
    return redirect('browse_works')

@login_required
def payment_failed(request):
    return render(request, 'payment_failed.html')
@login_required
def chat_with_artisan(request, artisan_id):
    artisan = Artisan.objects.get(pk=artisan_id)
    # Handle chat functionality with the artisan (e.g., integrate WhatsApp chat API)
    return render(request, 'chat.html', {'artisan': artisan})
