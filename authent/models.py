from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Department (models.Model):
    dep_code=models.CharField(max_length=50,primary_key=True)
    dep_name=models.CharField(max_length=100)
    def __str__(self):
        return self.dep_name

@python_2_unicode_compatible
class Employee (models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    department=models.OneToOneField(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
