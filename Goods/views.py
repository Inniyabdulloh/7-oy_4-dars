from django.shortcuts import render
from . import models

def main(request):
    products = models.Product.objects.all()
    banners = models.Banner.objects.filter(is_active = True)[:5]
    context = {}
    context['banners'] = banners
    context['products'] = products

    return render(request, 'index.html', context)
