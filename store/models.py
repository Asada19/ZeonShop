import re
from django.db import models
from colorfield.fields import ColorField
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from requests import Response
from django.core.exceptions import ValidationError


# Create your models here.


class Collection(models.Model):
    """ Модель колекции """
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='collection_image')

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """ Модель Продуктов """
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    colection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Коллекция',
                                  related_name='colection')
    articul = models.CharField(max_length=100, verbose_name='Артикул', blank=True, default='articul')
    description = RichTextField(verbose_name='Описание', blank=True, default='description')
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    sales = models.PositiveIntegerField(blank=True, default=0, verbose_name='Скидка')
    final_price = models.PositiveIntegerField(verbose_name='Итоговая цена')
    size = models.CharField(max_length=100, verbose_name='Размерный ряд, формат ввода: число-число', default='44-46')
    material = models.CharField(max_length=100, verbose_name='Материал', default='cotton')
    composition = models.CharField(max_length=100, verbose_name='Состав', default='cotton')
    favorite = models.BooleanField(verbose_name='Избранное')
    top_sales = models.BooleanField(verbose_name='Хит продаж')
    new_prod = models.BooleanField(verbose_name='Новинки')
    stock = models.PositiveIntegerField(verbose_name='Количество в линейке')

    def save(self, *args, **kwargs):
        """ функция рассчета количества товаров на основе регулярных выражений и срезов, формат ввода строго: n-n """
        try:
            numbers = re.split(r'-', self.size)
            result = list(range(int(numbers[0]), int(numbers[1]), 2))
        except ValidationError:
            raise ValidationError('Need to input data like: n-n')
        self.final_price = self.price * (100 - self.sales) / 100
        self.stock = len(result) + 1
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Image(models.Model):
    """ отдельный класс изображений для того что бы можно было добавлять множество изображений в одном продукте"""
    image = models.ImageField(upload_to='products', blank=True)
    color = ColorField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', )


class Callback(models.Model):
    """ Модель для Обратного звонка """
    name = models.CharField(max_length=150, unique=False, verbose_name="Имя")
    phone = PhoneNumberField(null=False, verbose_name="Tелефон")
    time = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Дата заявки")
    form = models.CharField(max_length=254, default='Обратный звонок', verbose_name='тип обращения')
    called = models.BooleanField(default=False, verbose_name='Перезвонили?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id", "-time"]
        verbose_name = 'Заявка на обратный звонок'


Status = (
    ('Оформлен', 'Оформлен'),
    ('Отменен', 'Отменен'),
    ('Новый', 'Новый'),
)


class Order(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    mail = models.CharField(max_length=50, null=True, blank=True, verbose_name='Почта')
    num = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер')
    country = models.CharField(max_length=30, null=True, blank=True, verbose_name='Страна')
    city = models.CharField(max_length=30, null=True, blank=True, verbose_name='Город')
    date_order = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Дата оформления')
    status = models.CharField(choices=Status,
                              max_length=255,
                              db_index=True,
                              default=('Новый', 'Новый'), verbose_name='Выбор из списка')
    # # Order info
    # sum = models.IntegerField(null=True, blank=True, default=0, verbose_name='Количество линеек')
    # sum_quantity = models.IntegerField(null=True, blank=True, default=0, verbose_name='Количество всех товаров в '
    #                                                                                   'линейках')
    # price = models.IntegerField(null=True, blank=True, default=0, verbose_name='Общая цена до учета скидок')
    # discounts = models.IntegerField(null=True, blank=True, default=0, verbose_name='Сумма всех скидок')
    # total = models.IntegerField(null=True, blank=True, default=0, verbose_name='Итого к оплате')
    # cart = models.ForeignKey(CartItem, on_delete=models.CASCADE)
        #
        # def save(self,  *args, **kwargs):
        #     self.sum_quantity = Product.stock
        #     self.price = Product.price
        #     self.discounts = Product.sales
        #     self.total = Product.final_price
        #     super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


# Оформление заказа
class CartItem(models.Model):
    cart = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart', blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True, default=1)
    user = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='user', blank=True)
    total = models.IntegerField(null=True, blank=True, default=0, verbose_name='Итого к оплате')

    def save(self, *args, **kwargs):
        self.total = self.cart.final_price
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user)


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product', blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField(default=True, null=True, blank=True, verbose_name='Cтоимость')
    stock = models.IntegerField(default=0, null=True, blank=True, verbose_name='Общ Количество в одной линейке:')
    sale = models.IntegerField(default=True, null=True, blank=True, verbose_name='Скидка')
    final_price = models.IntegerField(default=True, null=True, blank=True, verbose_name='Итого')
    image = Product.images
    name = models.CharField(max_length=200, blank=True, null=True, editable=False, verbose_name='Название товара')
    # cart = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cart', blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price
        self.stock = self.product.stock
        self.sale = self.price - self.product.final_price
        self.final_price = self.product.final_price * self.quantity
        self.name = self.product.name
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.product)


