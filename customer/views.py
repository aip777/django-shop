from django.shortcuts import render
from .models import Customer
# Create your views here.


def customerlistView(request):
    customer = Customer.objects.all()
    context = {
        'customer': customer, 
    }
    return render(request, 'customer/customer-list.html', context)