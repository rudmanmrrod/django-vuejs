from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  """!
  Clase para generar el modelo del perfil

  @author Rodrigo Boet (rudmanmrrod at gmail.com)
  @date 19-11-2018
  @version 1.0.0
  """
  
  dni_number = models.PositiveIntegerField()

  address = models.TextField()

  zip_code = models.PositiveIntegerField()

  gender = models.CharField(max_length=10,choices=(('M','MALE'),('F','FEMALE')))

  user = models.OneToOneField(User, on_delete=models.CASCADE)