from django.db import models
from phone_field import PhoneField

# Create your models here.


class UserType(models.Model):
    name = models.CharField(max_length=10)


class User(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
