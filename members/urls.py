from django.urls import path
from . import views

urlpatterns = [
    path('members/',views.members, name='members'),
    path('james/',views.james, name='james'),
]