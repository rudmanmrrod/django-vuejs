from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexTemplate.as_view()),
]