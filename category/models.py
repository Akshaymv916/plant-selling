from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category')
    description=models.TextField(null=True)

    def __str__(self) -> str:
        return self.category_name