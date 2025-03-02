from rest_framework import serializers
from .models import User, UserSettings
from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.utils import timezone

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=25, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        # Crear el usuario
        user = User.objects.create_user(**validated_data)

        # Crear los UserSettings para el nuevo usuario
        UserSettings.objects.create(user=user, notification=True, night_mode=False)

        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)  # Solo para entrada
    password = serializers.CharField(max_length=25, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        return obj.tokens()  # `obj` ya es el usuario

    class Meta:
        model = User
        fields = ['tokens']  # Solo devolver tokens

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = User.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            raise AuthenticationFailed('Invalid credentials, try again')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        user.last_login = timezone.now()
        user.save()
        return user  # Retornamos el usuario directamente

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = '__all__'