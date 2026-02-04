from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    LOCATION_CHOICES = [
        ('MUM', 'Mumbai'),
        ('NY', 'New York'),
        ('LDN', 'London'),
    ]
    location = models.CharField(max_length=255, choices=LOCATION_CHOICES, default='MUM')

    def __str__(self):
        return f"{self.username.username}'s Profile"

    class Meta:
        db_table = "user_profile"
        app_label = 'ess'