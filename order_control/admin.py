from django.contrib import admin
from .models import UserType, User, Product
# Register your models here.

admin.site.register(UserType)
admin.site.register(User)
admin.site.register(Product)
