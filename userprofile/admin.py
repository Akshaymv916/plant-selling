from django.contrib import admin

# Register your models here.
from userprofile.models import Address, Contactus

@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    list_display=['user','name','country','state','district']

@admin.register(Contactus)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=['user','name','email','msg','date']
