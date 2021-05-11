from django.urls import path
from .views import customerlistView

urlpatterns = [
    path('customer-list/', customerlistView, name='customer-list'),
    
]