from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Band
from listing.models import Listing
from django.shortcuts import render
from listing.forms import BandForm, ContactUsForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.http import JsonResponse



def band_list(request):
    
    ctx = {}
    url_parameter = request.GET.get("q")
    
    if url_parameter:
        bands = Band.objects.filter(name_icontains=url_parameter)
    else: 
        bands = Band.objects.all()
    
    ctx['bands'] = bands
    
    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest"  and does_req_accept_json
    
    if is_ajax_request:
        
        html = render_to_string(
            template_name='bands_results.html',  context={"bands" : bands}
        )
        data_dict = {'html_from_view': html}
        return JsonResponse(data=data_dict, safe=False)
    
    return render(request,
                  'bands/band_list.html',
                  {'bands': bands })
    
    
def band_detail(request, id):
       band = Band.objects.get(id=id)
       return render(request,
                     'bands/band_detail.html', 
                     context={'band': band })

def band_create(request):
    
    if request.method == 'POST':
        form = BandForm(request.POST)
        
        if form.is_valid():
            band = form.save()
            
            return redirect('band-detail', band.id)
        
    else:
        form = BandForm()
        
    return render(request,
                  'bands/band_create.html',
                  {'form' : form})
    
def band_update(request, id):
    band = Band.objects.get(id=id)
    
    if request.method == 'POST':
        form = BandForm(request.POST, instance = band)
        if form.is_valid():
            form.save()
            
        return redirect('band-detail', band.id)

    else:
        form = BandForm(instance = band)
    
    return render(request,
                  'bands/band_update.html',
                  {'form' : form})
    
def band_delete(request, id):
    band = Band.objects.get(id=id)
    
    if request.method == 'POST':
        band.delete()
        
        return redirect('band-list')
    
    return render(request,
                  'bands/band_delete.html',
                  {'band' : band})
    
    
def band_search(request):
    
    if request.method == 'GET':
        search = request.GET.get('search')
        bands = Band.objects.all().filter(name__contains = search)
        return render(request,
                      'bands/bands_results.html',
                      {'bands' : bands})
    

# ------------>    AJAX SEARCH <-------------------- 

    
#def band_search(request):
#    ctx = {}
#    url_parameter = request.GET.get("q")
#
#    if url_parameter:
#        artists = Artist.objects.filter(name__icontains=url_parameter)
#    else:
#        artists = Artist.objects.all()
#
#    ctx["artists"] = artists
#    does_req_accept_json = request.accepts("application/json")
#    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json
#
#    if is_ajax_request:
#    
#        html = render_to_string(
#            template_name="artists-results-partial.html", context={"artists": artists}
#        )
#        data_dict = {"html_from_view": html}
#        return JsonResponse(data=data_dict, safe=False)
#
#    return render(request, "artists.html", context=ctx) 
    
    
    
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
    
def listing_create(request):
    
    if request.method == 'POST':
        form = ListingForm()
        
        if form.is_valid():
            listing = form.save()
            
            return redirect('listing-detail', listing.id)
    
    else:
        form = ListingForm()
        
    return render(request,
                  'listings/listing_create.html',
                  {'form': form} )
    
def listing_update(request, id):
    listing = Listing.objects.get(id=id)
    
    if request.method == 'POST':
        form = ListingForm(request.POST, instance = listing)
        if form.is_valid():
            form.save()
            
        return redirect('listing-detail', listing.id)

    else:
        form = ListingForm(instance = listing)
    
    return render(request,
                  'listings/listing_update.html',
                  {'form' : form})
        

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



    


