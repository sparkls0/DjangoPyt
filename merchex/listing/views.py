from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Band
from listing.models import Listing
from django.shortcuts import render

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
    return render(request, 'contact/hello.html')


