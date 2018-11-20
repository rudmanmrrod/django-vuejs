from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexTemplate.as_view(), name='index'),
    path('create', CreateUserView.as_view(), name='user_profile_create'),
]