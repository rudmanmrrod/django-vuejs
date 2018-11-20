from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import TemplateView, FormView
from .forms import *
from .models import *

class IndexTemplate(TemplateView):
  """!
  Clase para cargar el index.html

  @author Rodrigo Boet (rudmanmrrod at gmail.com)
  @date 19-11-2018
  @version 1.0.0
  """
  template_name = "index.html"

class CreateUserView(FormView):
  """!
  Clase para registrar un usuario y su perfil

  @author Rodrigo Boet (rudmanmrrod at gmail.com)
  @date 19-11-2018
  @version 1.0.0
  """
  template_name = "create.user.html"
  form_class = RegisterForm

  def form_valid(self,form):
    """!
    Método si el formulario es válido

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 19-11-2018
    @param form Recibe como parámetro el formulario
    @version 1.0.0
    """
    user = User()
    user.username = form.cleaned_data['username']
    user.email = form.cleaned_data['email']
    user.first_name = form.cleaned_data['first_name']
    user.last_name = form.cleaned_data['last_name']
    user.set_password(form.cleaned_data['password1'])
    user.save()
    user_profile = UserProfile()
    user_profile.dni_number =  form.cleaned_data['dni_number']
    user_profile.address =  form.cleaned_data['address']
    user_profile.zip_code =  form.cleaned_data['zip_code']
    user_profile.gender =  form.cleaned_data['gender']
    user_profile.user = user
    user_profile.save()
    return JsonResponse({'message':'Create Successfully','valid':True})

  def form_invalid(self,form):
    """!
    Método si el formulario es inválido

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 19-11-2018
    @param form Recibe como parámetro el formulario
    @version 1.0.0
    """
    return JsonResponse({'error':form.errors,'valid':False})