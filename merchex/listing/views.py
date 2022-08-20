from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Band
from listing.models import Listing
from django.shortcuts import render
from listing.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'bands/band_list.html',
                  {'bands': bands })
    
    
def band_detail(request, id):
       band = Band.objects.get(id=id)
       return render(request,
                     'bands/band_detail.html', 
                     context={'band': band })
    
def about(request):
    return render(request, 'about/hello.html')

def listing_list(request):
     listings = Listing.objects.all()
     return render(request,
                   'listings/listing_list.html',
                   {'listings' : listings})
     
def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html',
                  context={'listing':listing })

def contact(request): 
    
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        
        if form.is_valid():
            send_mail(
                subject = f'Message from {form.cleaned_data["name"] or "anonyme" } via Merchex Contact Us Form',
                message = form.cleaned_data['message'],
                from_email = form.cleaned_data['email'],
                recipient_list = ['admin@merchex.xyz'],
            )
            return redirect('email-sent/')
    else:
        form = ContactUsForm()


    return render(request, 
                  'contact/contact.html',
                  {'form' : form })
    


def email_sent(request):
    return render(request, 'email/email-sent.html')



    


