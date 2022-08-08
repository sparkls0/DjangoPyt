from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Band
from listing.models import Listing
from django.shortcuts import render

def hello(request):
    bands = Band.objects.all()
    print(bands)
    return render(request,
                  'bands/hello.html',
                  {'bands' : bands})

def about(request):
    return render(request, 'about/hello.html')

def listings(request):
     listings = Listing.objects.all()
     return render(request,
                   'listings/hello.html',
                   {'listings' : listings})

def contact(request):
    return render(request, 'contact/hello.html')


