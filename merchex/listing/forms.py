from django import forms


class ContactUsForm(forms.Form):
    
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'contact-form-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'contact-form-input'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'contact-form-input'}))
    message = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'contact-form-message'}))
    
    
    
    
    
    
    