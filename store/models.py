import re
from django.db import models
from colorfield.fields import ColorField
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()



class Collection(models.Model):
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='collection_image') 

    # def get_absolute_url(self):
    #     return f"{self.id}/"

    

    def __str__(self) -> str:
        return self.name


class BuyerList(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    # phone = PhoneNumberField()
    country = CountryField(blank_label='(select country)')
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    status = models.BooleanField()




class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    colection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Коллекция', related_name='colection')
    articul = models.CharField(max_length=100, verbose_name='Артикул')
    description = RichTextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    sales = models.PositiveIntegerField(blank=True, default=0, verbose_name='Скидка')
    final_price = models.PositiveIntegerField(verbose_name='Итоговая цена')
    size = models.CharField(max_length=100, verbose_name='Размерный ряд в линейке')
    material = models.CharField(max_length=100, verbose_name='Материал')
    composition = models.CharField(max_length=100, verbose_name='Состав')
    favorite = models.BooleanField(verbose_name='Избранное')
    top_sales = models.BooleanField(verbose_name='Хит продаж')
    new_prod = models.BooleanField(verbose_name='Новинки')
    stock = models.PositiveIntegerField(verbose_name='Количество в линейке')
    
        
    def save(self, *args, **kwargs):    

        """ вариант счета количества товаров с регулярным выражением """
        numbers = re.split(r'-', self.size) 
        result = list(range(int(numbers[0]), int(numbers[1]), 2))
        self.final_price = self.price * (100 - self.sales) / 100
        self.stock = len(result) + 1
        super(Product, self).save(*args, **kwargs)
   

    

    def __str__(self):
        return self.name



class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    collections = models.ForeignKey(Collection, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    sales = models.PositiveIntegerField()
    final_price = models.PositiveIntegerField()


class Image(models.Model):
    image = models.ImageField(upload_to='products', blank=True)
    color = ColorField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images',)


class Callback(models.Model):
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






