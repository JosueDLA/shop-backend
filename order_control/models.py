from django.db import models
from phone_field import PhoneField

# Create your models here.


class UserType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OrderDetail(models.Model):
    quantity = models.IntegerField()
    price = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    date = models.DateField(auto_now=True)
    total_price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
