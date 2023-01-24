from django.db import models
from django.contrib import admin

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    # null=True -> enable upload info without specified value in this field
    date_created = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)    

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.name



class Order(models.Model):

    # Drop down menu
    STATUS = (
        ('Pending', 'Pending'), #(A,B) - A -> Value to be set, B -> value seen in the list
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    # on_delet -> what happen if we delete the record wchich has been inherited -> SET_NULL - will not delete any records
    # Example: If SET_NULL and we delete customer Robert, then all orders will not be deleted
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL) 
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL) 
    status = models.CharField(max_length=200, null=True, choices=STATUS)    
    date_created = models.DateTimeField(auto_now_add=True, null=True) 
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name

