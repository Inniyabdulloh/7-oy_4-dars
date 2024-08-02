from django.urls import path
from .views import BannerListView, BannerDetailView, BannerDeleteView, BannerUpdateView


urlpatterns = [
    path('list/', BannerListView.as_view(), name='banner-list'),
    path('detail/<str:code>/', BannerDetailView.as_view(), name='banner-detail'),
    path('delete/<str:code>/', BannerDeleteView.as_view(), name='banner-delete'),
    path('update/<str:code>/', BannerUpdateView.as_view(), name='banner-update'),
]