from django.urls import path
from . views import SignUpView, HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='login'),
    path('signup', SignUpView.as_view())
]