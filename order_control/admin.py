from django.contrib import admin
from .models import UserType, User, Product
# Register your models here.


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone', 'user_type')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'user')


admin.site.register(UserType, UserTypeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
