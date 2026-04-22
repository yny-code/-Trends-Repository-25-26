from django.urls import path
from . import views

utlpatterns = [
    path('members/', view members, name='members'),
]
