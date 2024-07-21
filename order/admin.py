from django.contrib import admin
from django.urls import reverse

from order.models import Cancelorder, Checkout, Order, Orderitem, Payment, Wishlist
from django.utils.html import format_html






@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display=['id','order_status','total_price','owner','order_date',]


@admin.register(Orderitem)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display=['id','productname','item_status','quantity','owner','delivery_date']
    def productname(self, obj):
        link = reverse("admin:product_products_change", args=[obj.product.id])
        return format_html('<a href="{}">{}</a>', link, obj.product.name)


@admin.register(Checkout)
class CheckoutModelAdmin(admin.ModelAdmin):
    list_display=['user_id','orderid','order','paymentid','status','phone','sub_total','order_date','paid','paymentmode']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['user','amount','paid']

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display=['user_id','product_id','add_date']

@admin.register(Cancelorder)
class CancelorderModelAdmin(admin.ModelAdmin):
    list_display=['order','reason','user']

