from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  
  dni_number = models.PositiveIntegerField()

  address = models.TextField()

  zip_code = models.PositiveIntegerField()

  gender = models.CharField(max_length=10,choices=(('M','MALE'),('F','FEMALE')))

  user = models.OneToOneField(User, on_delete=models.CASCADE)