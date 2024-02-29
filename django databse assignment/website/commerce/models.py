from django.db import models

# Create your models here.

class CompanyInformation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.type
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    type = models.ForeignKey(Type, on_delete= models.CASCADE, null=True) 
    image = models.ImageField(null = True)
    price= models.FloatField(null = True)
    date = models.DateField(auto_now_add=True, null = True)
    
    def __str__(self) -> str:
        return self.product_name

class FormSubmission(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
