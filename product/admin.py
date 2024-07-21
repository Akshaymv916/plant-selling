from django.contrib import admin

from product.models import Filter_Price, Product_review, Products




# Register your models head
admin.site.register( Filter_Price)



@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','name','stock','orginal_price','quantity']

@admin.register(Product_review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display=['user','item','ratings','review_desp']