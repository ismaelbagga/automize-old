from django import forms
from django.forms import ModelForm 
from . models import Contact , Subscribe



class ContactCreationForm(forms.ModelForm):

    class Meta :
        model = Contact
        fields = '__all__'

class NewcontactCreationForm(forms.Form):
   
    name = forms.CharField()
    email = forms.EmailField()
    Company = forms.CharField()
    Message = forms.CharField()
    chik  = forms.BooleanField()

class SubscribeCreartionForm(forms.ModelForm):
    
    # email = forms.EmailField()

    class Meta :
         model = Subscribe
         fields = '__all__'
