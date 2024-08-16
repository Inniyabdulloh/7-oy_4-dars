from django.shortcuts import render
from . import models

def main(request):
    banners = models.Banner.objects.all()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {
        'banners': banners,
        'products': products,
        'categories': categories,

    }
    try:
        info = models.Info.objects.get(is_active=True)
        context['info'] = info
    except models.Info.DoesNotExist:
        ...

    return render(request, 'index.html', context)
