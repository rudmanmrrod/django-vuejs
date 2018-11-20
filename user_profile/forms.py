from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
  """!
  Formulario para registrar el usuario

  @author Rodrigo Boet (rudmanmrrod at gmail.com)
  @date 19-11-2018
  @version 1.0.0
  """
  class Meta:
    model = User
    fields = ['password1', 'password2',
      'first_name', 'last_name', 'email', 'username']

  dni_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
        'placeholder': 'DNI Number', 'v-model': 'dni_number'}))
  
  address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Address', 'v-model': 'address'}))
  
  zip_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
        'placeholder': 'DNI Number', 'v-model': 'zip_code'}))

  gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'v-model': 'gender'}),
    choices = (('M','MALE'),('F','FEMALE')))

  def __init__(self, *args, **kwargs):
    """!
    Método para iniciar el formulario

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 19-11-2018
    @version 1.0.0
    """
    super().__init__(*args, **kwargs)

    self.fields['username'].widget.attrs.update(
      {'class': 'form-control', 'placeholder': 'Username', 'autofocus': False,
      'v-model': 'username'})

    self.fields['password1'].widget.attrs.update(
      {'class': 'form-control','placeholder': 'Password', 'v-model': 'password1'})
    self.fields['password1'].required = True
    self.fields['password2'].widget.attrs.update(
      {'class': 'form-control', 'placeholder':'Password Repeat', 'v-model': 'password2'})
    self.fields['password2'].required = True
    self.fields['email'].widget.attrs.update(
      {'class': 'form-control', 'placeholder': 'Email', 'v-model': 'email'})
    self.fields['email'].required = True
    self.fields['first_name'].widget.attrs.update(
      {'class': 'form-control','placeholder': 'First Name', 'v-model': 'first_name'})
    self.fields['first_name'].required = True
    self.fields['last_name'].widget.attrs.update(
      {'class': 'form-control', 'placeholder':'Last Name', 'v-model': 'last_name'})
    self.fields['last_name'].required = True

  def clean(self):
    """!
    Método para validar el formulario

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 19-11-2018
    @version 1.0.0
    """
    cleaned_data = super(RegisterForm, self).clean()
    email = cleaned_data.get("email")
    password1 = cleaned_data.get("password1")
    password2 = cleaned_data.get("password2")

    if password1 != password2:
      msg = "Password not match"
      self.add_error('password1', msg)

    if email:
      msg = "Error on mail: %s, has been used" % (email)
      try:
        User.objects.get(email=email)
        self.add_error('email', msg)
      except:
        pass