from datetime import timezone
from django.db import models

from category.models import Category
from home.models import Customuser
from django.db.models import Avg
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver

# Create your models here.


class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('100 TO 200', '100 TO 200'),
        ('200 TO 500', '200 TO 500'),
        ('500 TO 1000', '500 TO 1000'),
        ('1000 TO 2000', '1000 TO 2000'),
        ('2000 TO 50000', '2000 TO 5000'),
    )

    price = models.CharField(choices=FILTER_PRICE, max_length=60)

    def __str__(self):
        return self.price

class Products(models.Model):

    IN_STOCK=0
    OUT_OF_STOCK=1
    STOCK = ((IN_STOCK, 'IN_STOCK'), (OUT_OF_STOCK, 'OUT_OF_STOCK'))
    CONDITION = (('New', 'New'), ('Old', 'Old'))        
    name = models.CharField(max_length=100)
    desc=models.TextField(default=True)
    quantity = models.IntegerField(default=10)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer = models.DecimalField(max_digits=10, decimal_places=0)
    image1=models.ImageField(upload_to='product_images')
    image2=models.ImageField(upload_to='product_images',null=True,default=True)
    image3=models.ImageField(upload_to='product_images',null=True,default=True)
    image4=models.ImageField(upload_to='product_images',null=True,default=True)
    color=models.CharField(max_length=50)
    views=models.IntegerField(default=0)
    condtion = models.CharField(choices=CONDITION, max_length=100)
    stock = models.IntegerField(choices=STOCK,default=OUT_OF_STOCK)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)

    def orginal_price(self):
        orginal_price=self.price-(self.price*(self.offer/100))
        return round(orginal_price,2)
    def __str__(self):
        return str(self.name)
    def save(self, *args, **kwargs):
        if self.quantity <=0:
            self.stock=1
        else:
            self.stock=0
        super().save(*args, **kwargs)

    

class Product_review(models.Model):
    user=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    item=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='reviews')
    review_desp=models.TextField()
    ratings=models.IntegerField()
    review_date = models.DateField(auto_now_add=True, null=True)


        

    def __str__(self):
        return str(self.user)
    


