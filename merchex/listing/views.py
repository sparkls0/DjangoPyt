from pyexpat.errors import messages
from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Listing, Band

from django.contrib.auth.models import User, auth
from django.contrib import messages


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
    return render(request, 'about/about_us.html')

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


# ------------>   LOGIN  <-------------------- 


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('login-user')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
            

    else:
        return render(request, 'account/login.html')



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('band-list')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login-user')

    else:
        return render(request, 'account/login.html')
    
    
def logout_user(request):
    auth.logout(request)
    return redirect('band-list')


