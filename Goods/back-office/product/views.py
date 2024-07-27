# list ---
# detail ---
# create ---
# update ---
# delete ---
from django.views import View

from Goods import models
from django.shortcuts import render, redirect


def listProduct(request):
    queryset = models.Product.objects.all()
    context = {}
    context['queryset'] = queryset
    return render(request, 'back-office/product/list.html',context)


def detailProduct(request, id):
    queryset = models.Product.objects.get(id=id)
    context = {}
    print(models.ProductImg.objects.filter(product=queryset))
    context['queryset'] = queryset
    context['images'] = models.ProductImg.objects.filter(product=queryset)
    return render(request, 'back-office/product/detail.html',context)


def createProduct(request):
    context = {}
    context['categorys'] = models.Category.objects.all()
    if request.method == 'POST':
        # way 1
        # category_id = request.POST['category_id']
        # category = models.Category.objects.get(id=category_id)
        # product = models.Product.objects.create(
        #     name = request.POST['name'],
        #     quantity = request.POST['quantity'],
        #     price = request.POST['price'],
        #     category = category, 
        #     description = request.POST['description']
        # )
        # way 2
        product = models.Product.objects.create(
            name = request.POST['name'],
            quantity = request.POST['quantity'],
            price = request.POST['price'],
            category_id = request.POST['category_id'], 
            description = request.POST['description']
        )

        images = request.FILES.getlist('images')

        for image in images:
            models.ProductImg.objects.create(
                img = image,
                product = product
            )
    return render(request, 'back-office/product/create.html', context)


def deleteProduct(request, id):
    models.Product.objects.get(id=id).delete()
    return redirect('listProduct')


def productEnter(request, code):

    product = models.ProductEnter.objects.get(generate_code=code)
    products = models.Product.objects.all()
    context = {
        'products': products,
        'product': product
    }
    return render(request, 'back-office/product/product-enter.html', context)


class ProductEnterListView(View):
    def get(self, request):
        all_enters = models.ProductEnter.objects.all()
        context = {
            'products': all_enters
        }

        return render(request, 'back-office/product/product-enter-list.html', context)


class ProductEnterUpdateView(View):
    def get(self, request, code):
        product = models.ProductEnter.objects.get(generate_code=code)
        products = models.Product.objects.all()
        context = {
            'products': products,
            'product': product
        }
        return render(request, 'back-office/product/product-enter-update.html', context)

    def post(self, request, code):
        update_product = models.ProductEnter.objects.get(generate_code=code)

        product = models.Product.objects.get(generate_code=request.POST['product'])
        quantity = request.POST['quantity']
        description = request.POST['description']

        update_product.product = product
        update_product.quantity = int(quantity)
        # print(type(f" integermi? { quantity}"))

        update_product.description = description

        update_product.save()
        update_product.refresh_from_db()

        return redirect('enterProduct', code=code )


class AddProductEnterView(View):
    def get(self, request):
        products = models.Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'back-office/product/product_enter-add.html', context )
    def post(self, request):

        product = request.POST['product']
        product = models.Product.objects.get(generate_code=product)
        quantity = request.POST['quantity']
        description = request.POST['description']

        models.ProductEnter.objects.create(
            product=product,
            quantity=int(quantity),
            description=description
        )
        return redirect('product-enter-list')
