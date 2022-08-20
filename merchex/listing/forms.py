from django import forms


class ContactUsForm(forms.Form):
    
    name = forms.CharField(required=False)
    email = forms.EmailField()
    phone = forms.CharField(required=False)
    message = forms.CharField(max_length=1000)
    
    
    
    
    
    
    