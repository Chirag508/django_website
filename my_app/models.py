from django.db import models

# Create your models here.
class blog(models.Model):
    author = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    published_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    def __str__(self):
        return self.author

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    message = models.TextField()
    date_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    Create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def total(self):
        return self.price * self.quantity
        
    def __str__(self):
        return self.name