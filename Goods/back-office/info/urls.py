from django.urls import path
from .views import InfoListView, InfoCreateView, InfoDetailView, InfoUpdateView, InfoDeleteView

urlpatterns = [
    path('list/', InfoListView.as_view(), name='info-list'),
    path('create/', InfoCreateView.as_view(), name='info-create'),
    path('<str:code>/', InfoDetailView.as_view(), name='info-detail'),
    path('<str:code>/delete/', InfoDeleteView.as_view(), name='info-delete'),
    path('<str:code>/update/', InfoUpdateView.as_view(), name='info-update'),
]