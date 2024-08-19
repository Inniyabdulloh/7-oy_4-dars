from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.ProductListAPIView.as_view()),
    path('product-detail/<str:code>/', views.ProductDetailAPIView.as_view()),
    path('category-list/', views.CategoryListAPIView.as_view()),
    path('category-detail/<str:code>/', views.CategoryDetailAPIView.as_view()),
    path('user-register/', views.UserCreateAPIView.as_view()),
    path('user-login/', views.UserLoginAPIView.as_view()),
    path('cart/', views.CartAPIView.as_view()),
    path('cart/add-product/<str:code>/', views.AddToCartAPIView.as_view()),
    path('cart/remove-product/<str:code>/', views.RemoveProductFromCartAPIView.as_view()),
]