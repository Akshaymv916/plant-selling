from django.contrib import admin

from product.models import Product_review

from .models import *
# Register your models here.



@admin.register(Customuser)
class CustomuserModelAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','number','is_verified']
