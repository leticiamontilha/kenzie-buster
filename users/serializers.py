from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
import ipdb


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="username already taken.")]),
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), 
                message="email alrady registered.")]),
    birthdate = serializers.DateField(default=None),
    first_name = serializers.CharField(),
    last_name = serializers.CharField(),
    password = serializers.CharField(write_only=True),
    is_employee = serializers.BooleanField(default=False),
    is_superuser = serializers.BooleanField(read_only=True, default=False)

    def create(self, validated_data: dict):
        print(validated_data)
        if validated_data['is_employee']:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)