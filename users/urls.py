from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    # Enable URL authorization by default
    path('', include('django.contrib.auth.urls')),
    # Page for registration
    path('register/', views.register, name='register')
]