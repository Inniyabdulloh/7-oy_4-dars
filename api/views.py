from django.contrib.auth import authenticate
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from Goods import models
from . import serializers
from Goods.models import Product, Category
from rest_framework.authtoken.models import Token
# Create your views here.

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = serializers.ProductListSerializer(products, many=True)
        return Response(serializer.data)



class ProductDetailAPIView(APIView):
    def get (self, request, code):
        product = Product.objects.get(code=code)
        serializer = serializers.ProductDetailSerializer(product)
        return Response(serializer.data)


class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = serializers.CategoryListSerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetailAPIView(APIView):
    def get (self, request, code):
        category = Category.objects.get(code=code)
        serializer = serializers.CategoryDetailSerializer(category)
        return Response(serializer.data)


class UserCreateAPIView(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    def post(self, request):
       username = request.data.get('username')
       password = request.data.get('password')
       user = authenticate(request, username=username, password=password)
       print(user)
       if user:
           token_key, _ = Token.objects.get_or_create(user=user)
           user_serializer = serializers.UserSerializer(user)
           context = {
                'message': "User logged in",
                'username': user_serializer.data.get("username"),
                'key': token_key.key
                   }
       else:
           context = {
               'message': "User not logged in",
           }

       return Response(context)


class CartAPIView(APIView):
    # @permission_classes(TokenAuthentication)
    # @authentication_classes(permissions.IsAuthenticated)
    def get(self, request):

        cart, _ = models.Cart.objects.get_or_create(
            author=request.user,
            is_active=True)

        products = models.CartProduct.objects.filter(cart=cart)
        cart_serializer = serializers.CartSerializer(products)
        product_serializer = serializers.CartProductsSerializer(products, many=True)
        context = {
            'products': product_serializer.data,
            'cart': cart_serializer.data,
        }

        return Response(context)


class AddToCartAPIView(APIView):
    def post(self, request, code):
        product = models.Product.objects.get(generate_code=code)
        cart, _ = models.Cart.objects.get_or_create(author=request.user, is_active=True)
        try:
            cart_product = models.CartProduct.objects.get(cart=cart, product=product)
            cart_product.quantity += 1
            cart_product.save()
            return Response({'message': "Product has been added to cart"}, status=status.HTTP_201_CREATED)
        except:
            models.CartProduct.objects.create(
                product=product,
                cart=cart,
                quantity=1
            )

            return Response({'message': "Product has been added +1 to cart"}, status=status.HTTP_201_CREATED)