from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import UserType, User
from .models import Product
from .models import OrderDetail, Order
from .serializers import UserSerializer
from .serializers import UserTypeSerializer
from .serializers import ProductSerializer
from .serializers import OrderDetailSerializer
from .serializers import OrderSerializer

# Create your views here.


class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all().order_by('name')
    serializer_class = UserTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all().order_by('quantity')
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('date')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
