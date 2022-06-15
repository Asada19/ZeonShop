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
    image = models.ImageField()
    blank = models.TextField()


class News(models.Model):
    image = models.ImageField(upload_to='News', verbose_name='Фото')
    title = models.CharField(max_length=254, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    def __str__(self) -> str:
        return self.title