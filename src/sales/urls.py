from django.urls import path
from .views import home

app_name = 'sales'

urlpatterns = [
    path('', home, name='home'),  
]
