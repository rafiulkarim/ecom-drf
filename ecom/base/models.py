from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=False)
    category = models.CharField(max_length=200, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=False, null=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200, null=True, blank=False)
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    comment = models.TextField(null=True, blank=False)
    _id = models.AutoField(primary_key=True, editable=False) 

    def __str__(self) -> str:
        return self.rating
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    payment = models.CharField(max_length=200, null=True, blank=False)
    taxprice = models.DecimalField(max_digits=7, decimal_places=2)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeliverd = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False) 

    def __str__(self) -> str:
        return str(self.createdAt)
    

class Orderitem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200, null=True, blank=False)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.CharField(max_length=255, null=True, blank=False)
    _id = models.AutoField(primary_key=True, editable=False) 

    def __str__(self) -> str:
        return self.name
    

class ShippiingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length=200, null=True, blank=False)
    city = models.CharField(max_length=200, null=True, blank=False)
    postalCode = models.CharField(max_length=100, null=True, blank=False)
    country = models.CharField(max_length=100, null=True, blank=False)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2)
    _id = models.AutoField(primary_key=True, editable=False) 

    def __str__(self) -> str:
        return self.address
    
