from datetime import timedelta, timezone
from django.db import models
from django.dispatch import receiver

from home.models import Customuser
from product.models import Products
from django.db.models.signals import pre_save

from userprofile.models import Address


class Order(models.Model):
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_SHIPPED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_CONFIRMED,'ORDER_CONFIRMED'),
                   (ORDER_SHIPPED,'ORDER_SHIPPED'),
                   (ORDER_DELIVERED,'ORDER_DELIVERED'),
                   (ORDER_REJECTED,'ORDER_REJECTED'),
                   )
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    address=models.ForeignKey(Address,on_delete=models.SET_NULL,null=True,blank=True)
    total_price=models.TextField(default=0)
    owner=models.ForeignKey(Customuser,on_delete=models.SET_NULL,null=True,related_name='orders')
    order_date = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.owner}'s order {self.id}"



class Wishlist(models.Model):
    user_id=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    add_date=models.DateField(auto_now_add=True)
    product_id=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.user_id}'s wishlist"
    
    
    
    

class Checkout(models.Model):
    PENDING=0
    ACCEPTED=1
    DELIVERED=2
    SUCCESSED=3
    REJECTED=4
    STATUS_CHOICES=((ACCEPTED,'ACCEPTED'),
                   (DELIVERED,'DELIVERED'),
                   (SUCCESSED,'SUCCESSED'),
                   (REJECTED,'REJECTED'))
    user_id = models.ForeignKey(Customuser, on_delete=models.CASCADE, null=True)
    phone=models.IntegerField(default=0)
    status=models.IntegerField(choices=STATUS_CHOICES,default=PENDING)
    orderid=models.CharField(max_length=300,null=True,blank=True)
    paymentid=models.CharField(max_length=200,null=True,blank=True)
    sub_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, null=True
    )
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    payable_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    paid=models.BooleanField(default=False)
    paymentmode=models.CharField(default="Cash on delivery",max_length=20)

    order_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"Checkout={self.id},{self.order}"
    
    
    
class Orderitem(models.Model):
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_SHIPPED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_CONFIRMED,'ORDER_CONFIRMED'),
                   (ORDER_SHIPPED,'ORDER_SHIPPED'),
                   (ORDER_DELIVERED,'ORDER_DELIVERED'),
                   (ORDER_REJECTED,'ORDER_REJECTED'),
                   )
    product=models.ForeignKey(Products,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
    item_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    delivery_date = models.DateField(null=True, blank=True)
    Checkout=models.ForeignKey(Checkout,on_delete=models.CASCADE,related_name='chekout',null=True,blank=True)


    def __str__(self):
        return f"{self.product} order id {self.id}"

@receiver(pre_save, sender=Orderitem)
def update_delivery_date(sender, instance, **kwargs):
    if not instance.delivery_date:
        instance.delivery_date = instance.owner.order_date + timedelta(days=10)

    

    

class Payment(models.Model):
    user=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    paid=models.BooleanField(default=False)


class Cancelorder(models.Model):
    order = models.ForeignKey(Orderitem, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Customuser, on_delete=models.SET_NULL, null=True)
    reason = models.TextField(null=True, blank=True)
    request_date = models.DateField(auto_now_add=True, null=True)
    return_date = models.DateField(null=True, blank=True)

    
    
