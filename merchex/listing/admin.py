from re import L
from django.contrib import admin

from listing.models import Band
from listing.models import Listing


class BandAdmin(admin.ModelAdmin):
    list_display = ('id','name','year_formed','genre', 'active')
    
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','type','sold','band')
    
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)




