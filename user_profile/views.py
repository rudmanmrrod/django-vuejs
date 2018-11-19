from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import TemplateView, FormView
from .forms import *
from .models import *

class IndexTemplate(TemplateView):
  template_name = "index.html"

class CreateUserView(FormView):
  template_name = "create.user.html"
  form_class = RegisterForm

  def form_valid(self,form):
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
    return JsonResponse({'message':'Create Successfully'})

  def form_invalid(self,form):
    return JsonResponse({'error':form.errors})
    return super().form_invalid(form)