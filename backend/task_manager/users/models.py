from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=25, unique=True)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    notification = models.BooleanField(default=True)
    night_mode = models.BooleanField(default=False)

    def __str__(self):
        return f'{User.username} settings: {self.notification} - {self.night_mode}'
