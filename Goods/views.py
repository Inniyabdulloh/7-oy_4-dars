from django.shortcuts import render
from . import models

def main(request):
    banners = models.Banner.objects.all()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    info = models.Info.objects.get(is_active=True)
    context = {
        'banners': banners,
        'products': products,
        'categories': categories,
        'info': info,
    }
    return render(request, 'index.html', context)
