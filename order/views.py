from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import AddOrderForm, EditOrderForm
from customer.models import Customer
from product.models import Products
from .models import Order
from customer.forms import AddCustomerForm

# @login_required()
def addOrderView(request):
    if request.method == 'POST':
        form = AddOrderForm(request.POST, request.FILES)
        customer =  AddCustomerForm(request.POST, request.FILES)

        product_obj = request.POST['products']
        if form.is_valid() and customer.is_valid():
            form_obj = form.save(commit=False)
            form_obj.customer = Customer.objects.latest('id')
            product = form.cleaned_data["products"]

            for product_obj in product:
                product_qy = Products.objects.filter(id=product_obj.id)

                for obj in product_qy:
                    if obj.current_stock>0:
                        print("Okay")
                    else:
                        messages.success(request, "Product not available")
                        return HttpResponseRedirect("#") 
            customer.save()
            form_obj.save()
            form.save_m2m()
            messages.success(request, 'Successfully added')
            return redirect('order-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#") 
    else:
        form = AddOrderForm()
        customer = AddCustomerForm()
        
    context = {
        'form': form,
        'customer':customer
    }
    return render(request, 'order/add-order.html', context)


# @login_required()
def orderlistView(request):
    order = Order.objects.all()


    # Order.products.through.objects.all()
    # print("__________p1",p1)

    amount = {}
    list_li = []
    for order_item in order:
        for obj in order_item.products.filter(order = order_item.id):
            list_li.append(obj.price)
        amount[order_item.id] = sum(list_li)
        list_li.clear()

    #     print("___order_id____",order_id)
    #     for products in Order.products.through.objects.all(): 
    #         id_order = products.order_id

    #         print(products.order_id)
    ojb = amount.values()
    order_list = zip(order,ojb)
   
    context = {
        'order': order_list
    }
    return render(request, 'order/order-list.html', context)

# @login_required()
def orderUpdateView(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = EditOrderForm(request.POST, request.FILES, instance=order)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect('order-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        form = EditOrderForm(instance=order)
    context = {
        'form': form,
    }
    return render(request, 'order/order-update.html', context)


# @login_required()
def deleteOrderView(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('order-list')


def orderDetailsView(request, id):
    order = get_object_or_404(Order, id=id)
    
    amount = {}
    list_li = []
   
    for obj in order.products.filter(order = order.id):
        list_li.append(obj.price)
    amount[order.id] = sum(list_li)
    list_li.clear()

    customer = Customer.objects.filter(id = order.customer.id )
    obj = amount.values()
    print(obj)
   
    print(order) 
    context = {
        'customer':customer,
        'obj':obj,
        'order': order
    }
    return render(request, 'order/order-details.html', context)