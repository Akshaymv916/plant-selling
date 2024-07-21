from django.db import models
from home.models import Customuser

# Create your models here.
class Address(models.Model):
    user=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    landmark=models.CharField(max_length=300)
    pincode=models.IntegerField(max_length=6)

    def __str__(self) -> str:
        return f"{self.name}'s Address "
    
class Contactus(models.Model):
    user=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    msg=models.TextField()
    date=models.DateField(auto_now_add=True)
    