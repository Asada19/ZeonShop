from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField


# Create your models here.
# class CallBack(models.Model):
#     name = models.CharField(max_length=254)
#     # phone = PhoneNumberField()
#     created_at = models.DateTimeField()
#     type = models.CharField(max_length=254)
#     status = models.BooleanField()


class Slider(models.Model):
    blank = models.URLField(blank=True ,null=True, verbose_name='Поле для ссылки')


class SliderImage(models.Model):
    image = models.ImageField(upload_to='sliders', blank=True, null=True)
    product = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='sliders_images')



class News(models.Model):
    image = models.ImageField(upload_to='News', verbose_name='Фото')
    title = models.CharField(max_length=254, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    def __str__(self) -> str:
        return self.title