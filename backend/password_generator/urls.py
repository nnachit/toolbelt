from django.urls import path
from password_generator.views import generate

urlpatterns = [
    path('', generate, name='generate'),
]