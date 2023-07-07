from django.urls import path
from . import views

urlpatterns = [
    path('greetings/', views.greetings),
    path('greetings/', views.greetings),
]