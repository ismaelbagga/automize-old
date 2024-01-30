from logging import info
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import * 
from automize.settings import EMAIL_HOST_USER
from .models import Contact , Subscribe
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import SubscribeCreartionForm
# Create your views here.

# Create your views here.

def subscribe(request):
    form = SubscribeCreartionForm()
    
    if request.method == 'POST':
         
        form = SubscribeCreartionForm(request.POST)
        email_value = request.POST.get('email', None)
        if form.is_valid() :           
            modal : Subscribe = form.save() 
            messages.info(request, "Thanks for reaching Us! We will get back you soon ...!")
            send_mail(
                    'Welcome to My Site',
                    'Thank you for creating an account!',
                    settings.EMAIL_HOST_USER,  # 'from_email'
                    [modal.email],  # 'recipient_list'
                )           
            return redirect('subscribe')
        if email_value is not None:
                if Subscribe.objects.filter(email=email_value).exists():
                    messages.error(request, "This email address is already in use.") 
               

    return render(request, 'amStaticApp/home.html',{'form' : form })

def home_view(request):
            
    return render(request, 'amStaticApp/home.html')


def about_view(request):
    return render(request, 'amStaticApp/about.html')


def blog_view(request):
    return render(request, 'amStaticApp/blog.html')


def blog_sample_view(request):
    return render(request, 'amStaticApp/blog_sample.html')


def contact_view(request):
    form = ContactCreationForm()
    submitted = False
    if request.method == 'POST':
        form = ContactCreationForm(request.POST)
       
        if form.is_valid() :
            modal : Contact = form.save()
            messages.success(request , "Thanks for  reaching Us! We will get back you soon ...!")
            send_mail(modal.name ,modal.Message,settings.EMAIL_HOST_USER,[modal.email])
            return redirect('contact')


    return render(request, 'amStaticApp/contact.html',{'form' : form })


def portfolio_view(request):
    return render(request, 'amStaticApp/portfolio.html')


def portfolio_sample_view(request):
    return render(request, 'amStaticApp/portfolio_sample.html')


def services_view(request):
    return render(request, 'amStaticApp/services.html')


def service_design_sample_view(request):
    return render(request, 'amStaticApp/service_design_sample.html')


def service_tech_sample_view(request):
    return render(request, 'amStaticApp/service_tech_sample.html')