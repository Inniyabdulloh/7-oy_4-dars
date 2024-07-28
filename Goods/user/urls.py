from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.myCart, name='myCart'),
    path('add-product-to-cart/<str:code>/', views.addProductToCart, name='addProductToCart'),
    path('create-order/<str:code>/', views.CreateOrder, name='createOrder'),
    path('delete/<str:code>/', views.deleteProductCart, name='deleteProductCart'),
]