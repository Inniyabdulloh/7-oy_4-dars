from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.myCart, name='myCart'),


    path('delete/<str:code>/', views.deleteProductCart, name='deleteProductCart'),
]