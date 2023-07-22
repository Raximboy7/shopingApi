from django.db import models
# from phonenumber_field.formfields import PhoneNumberField

# Create your models here.

class Category(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=120)
    img = models.ImageField()

    def __str__(self):
        return self.name
    


class Product(models.Model):
    slug = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField(max_length=2000)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Buy(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    
    def __str__(self):
        return self.product.title
    