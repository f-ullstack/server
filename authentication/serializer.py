from api.models import User, Profile

from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt_serializers import TokenObtainPairSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'fullName', 'email']

class MyTokenObtainPairSerializer (TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['firstName'] = user.firstName
        token['lastName'] = user.lastName
        token['fullName'] = user.fullName
        token['email'] = user.email

        return token