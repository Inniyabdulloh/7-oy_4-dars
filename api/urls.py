from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.ProductListView.as_view()),
    path('product-detail/<str:code>/', views.ProductDetailView.as_view()),
    path('category-list/', views.CategoryListView.as_view()),
    path('category-detail/<str:code>/', views.CategoryDetailView.as_view()),
    path('user-register/', views.UserRegisterView.as_view()),
    path('user-login/', views.UserLoginView.as_view()),
]