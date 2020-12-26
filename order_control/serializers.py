from rest_framework import serializers
from .models import UserType, User


class UserTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
