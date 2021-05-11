from django.urls import path
from .views import (
    addCategoryView, 
    categoryUpdateView, 
    categorylistView, 
    deleteCategoryView,

    addProductView,
    productslistView,
    productsUpdateView,
    deleteProductView
)

urlpatterns = [
    path('add-category/', addCategoryView, name='add-category'),
    path('add-category/<int:id>/', categoryUpdateView, name='category-update'),
    path('category-list/', categorylistView, name='category-list'),
    path('delete-category/<int:id>/', deleteCategoryView, name='delete-category'),

    path('add-product/', addProductView, name='add-product'),
    path('add-product/<int:id>/', productsUpdateView, name='product-update'),
    path('', productslistView, name='products-list'),
    path('delete-product/<int:id>/', deleteProductView, name='delete-product'),
    
]