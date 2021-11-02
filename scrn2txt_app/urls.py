from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.send_file, name='scan'),
]