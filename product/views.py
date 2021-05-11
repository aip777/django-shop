from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import AddCategoryForm,EditCategoryForm, AddProductsForm, EditProductsForm
from .models import Category, Products
 
# @login_required()
def addCategoryView(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added')
            return redirect('category-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        form = AddCategoryForm()
        
    context = {
        'form': form,
    }
    return render(request, 'category/add-category.html', context)


# @login_required()
def categorylistView(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'category/category-list.html', context)

# @login_required()
def categoryUpdateView(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = EditCategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect('category-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        form = EditCategoryForm(instance=category)
    context = {
        'form': form,
    }
    return render(request, 'category/category-update.html', context)


# @login_required()
def deleteCategoryView(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('category-list')


def addProductView(request):
    if request.method == 'POST':
        form = AddProductsForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added')
            return redirect('products-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        form = AddProductsForm()
        
    context = {
        'form': form,
    }
    return render(request, 'products/add-product.html', context)


# @login_required()
def productslistView(request):
    products = Products.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products-list.html', context)

# @login_required()
def productsUpdateView(request, id):
    products = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        form = EditProductsForm(request.POST, request.FILES, instance=products)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect('products-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        form = EditProductsForm(instance=products)
    context = {
        'form': form,
    }
    return render(request, 'products/product-update.html', context)


# @login_required()
def deleteProductView(request, id):
    products = get_object_or_404(Products, id=id)
    products.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('products-list')



       