from itertools import product

from django.db import models
from django.contrib.auth.models import User
from random import sample
import string


class GenerateCode(models.Model):
    generate_code = models.CharField(max_length=255, blank=True, primary_key=True)

    def __str__(self):
        return self.generate_code

    def save(self, *args, **kwargs):
        if not self.generate_code:
            self.generate_code = "".join(sample(string.ascii_letters, 20))
        super(GenerateCode, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Banner(GenerateCode):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Category(GenerateCode):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='categories/', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.generate_code:
            self.generate_code = "".join(sample(string.ascii_letters, 20))
        super(Category, self).save(*args, **kwargs)


class Product(GenerateCode):
    name: str = models.CharField(max_length=255)
    quantity: int = models.PositiveIntegerField(default=1)
    price: float = models.DecimalField(max_digits=8, decimal_places=2)
    category: Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description: str = models.TextField()
    image = models.ImageField(upload_to='products/', null=True)


    def __str__(self):
        return self.name

    @property
    def img_url(self):
        return ProductImg.objetcs.get(product=self).img.url


    @property
    def images(self):
        images = ProductImg.objects.filter(product=self)
        return images
    @property
    def is_like(self):
        products = WishList.objects.filter(product=self)
        return products

    @property
    def like_users(self):
        users = []
        products = WishList.objects.filter(product=self)
        if products:
            for user in products:
                users.append(user.user)
        return users

class ProductImg(GenerateCode):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='imgs')
    img = models.ImageField(upload_to='product-img')

    def __str__(self):
        return self.product.name

    @property
    def img_url(self):
        return self.img


class Cart(GenerateCode):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    shopping_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.author.username


class CartProduct(GenerateCode):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name


class Order(GenerateCode):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(
        choices=(
            (1, 'Tayyorlanmoqda'),
            (2, 'Yo`lda'),
            (3, 'Yetib borgan'),
            (4, 'Qabul qilingan'),
            (5, 'Qaytarilgan'),
        )
    )

    def __str__(self):
        return self.full_name


class ProductEnter(GenerateCode):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    old_quantity = models.IntegerField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        if not self.generate_code:
            self.old_quantity = self.product.quantity
            self.product.quantity += self.quantity
        else:
            self.product.quantity -= ProductEnter.objects.get(generate_code=self.generate_code).quantity
            self.product.quantity += self.quantity

        self.product.save()
        super(ProductEnter, self).save(*args, **kwargs)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Info(GenerateCode):
     phone = models.CharField(max_length=20, null=True, blank=True)
     address = models.CharField(max_length=255, null=True, blank=True)
     facebook = models.CharField(max_length=255, null=True, blank=True)
     twitter = models.CharField(max_length=255, null=True, blank=True)
     linkedin = models.CharField(max_length=255, null=True, blank=True)
     is_active = models.BooleanField(default=False)


     @property
     def photos(self):
         photos = InfoInstaPhoto.objects.filter(info=self)
         return photos

class InfoInstaPhoto(GenerateCode):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')