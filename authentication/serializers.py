from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration and update"""

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Create a new user with encrypted password"""
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    """Serializer for user login"""
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class LogoutSerializer(serializers.Serializer):
    """Serializer for logout (JWT token blacklisting)"""
    refresh = serializers.CharField()

    def validate(self, data):
        """Blacklist refresh token on logout"""
        try:
            token = RefreshToken(data["refresh"])
            token.blacklist()
        except Exception as e:
            raise serializers.ValidationError("Invalid token")
        return data

class PasswordResetSerializer(serializers.Serializer):
    """Serializer for requesting a password reset"""
    email = serializers.EmailField()

