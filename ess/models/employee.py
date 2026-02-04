from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    emp_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    department = models.CharField(max_length=100,null=True,blank=True)
    official_email = models.EmailField(max_length=100,null=True,blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emp_code} - {self.name}"        

    class Meta:
        db_table = "employee"
        app_label = 'ess'    