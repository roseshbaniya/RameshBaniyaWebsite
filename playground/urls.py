from django.urls import path
from . import views

# ucl configuration
urlpatterns = [
    path('hello/', views.say_hello)
]
