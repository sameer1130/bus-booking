from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "full_name",
            "first_name",
            "last_name",
            "email",
            "phone",
        )
        
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "password",
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate_phone(self, value):
        if User.objects.get(phone=value).exists():
            raise serializers.ValidationError("Phone number exists")
        return value
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
