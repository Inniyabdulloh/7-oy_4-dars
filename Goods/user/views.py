from django.shortcuts import render, redirect
from django.views import View

from Goods import models
from Goods.models import CartProduct


def myCart(request):

    try:
        cart, _ = models.Cart.objects.get_or_create(
            author=request.user,
            is_active=True)
        products = CartProduct.objects.filter(cart=cart)
        context = {
            'products': products,
            'cart': cart,
        }

    except:
        context = {}

    return render(request, 'back-office/user/cart.html', context)


def addProductToCart(request, code):
    product = models.Product.objects.get(generate_code=code)
    cart, _ = models.Cart.objects.get_or_create(author=request.user, is_active=True)
    try:
        cart_product = models.CartProduct.objects.get(cart=cart, product=product)
        cart_product.quantity+=1
        cart_product.save()
    except:
        models.CartProduct.objects.create(
            product=product, 
            cart=cart,
            quantity=1
        )
    return redirect('index')


def substractProductFromCart(request):
    code = request.GET['code']
    quantity = request.GET['quantity']
    product_cart = models.CartProduct.objects.get(generate_code=code)
    product_cart.quantity -= quantity
    product_cart.save()
    if not product_cart.quantity:
        product_cart.delete()
    return redirect('/')


def deleteProductCart(request, code):
    product_cart = models.CartProduct.objects.get(generate_code=code)
    product_cart.delete()
    return redirect('myCart')


def CreateOrder(request, code):
    cart = models.Cart.objects.get(
        generate_code=code
        )
    
    cart_products = models.CartProduct.objects.filter(cart=cart)

    done_products = []

    for cart_product in cart_products:
        if cart_product.quantity <= cart_product.product.quantity:
            cart_product.product.quantity -= cart_product.quantity
            cart_product.product.save()
            done_products.append(cart_product)
        else:
            for product in done_products:
                product.product.quantity += product.quantity
                product.product.save()
            raise ValueError('Qoldiqda kamchilik')

    models.Order.objects.create(
        cart=cart,
        full_name = f"{request.user.first_name}, {request.user.last_name}",
        email = request.user.email,
        status = 1
        )
    cart.is_active = False
    cart.save()
    
    return redirect('index')

class VishListView(View):
    def get(self, request):
        wish_list = models.WishList.objects.filter(user=request.user)
        context = {
            'wish_list': wish_list
        }
        return render(request, 'back-office/user/wish-list.html', context)


class AddWishListView(View):
    def get(self, request, code):
        product = models.Product.objects.get(generate_code=code)
        data, is_create = models.WishList.objects.get_or_create(
            user=request.user,
            product=product,
        )
        if not is_create:
            data.delete()

        return redirect('index')

