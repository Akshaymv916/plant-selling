from django.db import models

# Create your models here.

# Create your models here.

class Customuser(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    is_verified = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    profilepic=models.ImageField(upload_to='profilepic',null=True)
    joindate=models.DateField(auto_now_add=True, null=True)
    password = models.CharField(max_length=255,null=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    otp=models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    



