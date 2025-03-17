from django.db import models
import datetime

class Category(models.Model):
    name=models.CharField(max_length=50)
    
    def__str__(self):
        return self.name

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    password=models.PasswordField(max_length=50)
     
    def__str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalFieldField(default=10,decimal_places=2,max_digits)
    category=
    description=
    image=
    
    def__str__(self):
        return self.name

class Order(models.Model):