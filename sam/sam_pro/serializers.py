from rest_framework import serializers
from .models import Login



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(error_messages={'blank': 'username can not be blank'},required=True)
    password = serializers.CharField(error_messages={'blank': 'Password can not be blank'},required=True)
    class Meta:
        model = Login
        fields = ['username','password']

