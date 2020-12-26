from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import UserType, User
from .serializers import UserSerializer
from .serializers import UserTypeSerializer

# Create your views here.


class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all().order_by('name')
    serializer_class = UserTypeSerializer
    permissions_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
