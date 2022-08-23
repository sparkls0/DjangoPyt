from django import forms

from listing.models import Band, Listing

class ContactUsForm(forms.Form):
    
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'contact-form-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'contact-form-input'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'contact-form-input'}))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'contact-form-message', 'rows': 3 }))
    
    

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        exclude = ('url',)
        
class ListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = '__all__'
          

    
    
    