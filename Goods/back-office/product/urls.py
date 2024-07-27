from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createProduct, name='createProduct'),
    path('list', views.listProduct, name='listProduct'),
    path('enterdetail/<str:code>/', views.productEnter, name='enterProduct'),
    path('enterupdate/<str:code>/', views.ProductEnterUpdateView.as_view(), name='product-enter-update'),
    path('enterproductadd/', views.AddProductEnterView.as_view(), name='add-product-enter'),
    path('detail/<int:id>/', views.detailProduct, name='detailProduct'),
    path('delete/<int:id>/', views.deleteProduct, name='deleteProduct'),
    path('enter-list/', views.ProductEnterListView.as_view(), name='product-enter-list'),
]