from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField


class Slider(models.Model):
    blank = models.URLField(blank=True ,null=True, verbose_name='Поле для ссылки')


class SliderImage(models.Model):
    image = models.ImageField(upload_to='sliders', blank=True, null=True)
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='sliders_images')


class News(models.Model):
    image = models.ImageField(upload_to='News', verbose_name='Фото')
    title = models.CharField(max_length=254, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Новости'

    def __str__(self) -> str:
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=254, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'О нас'


    def __str__(self):
        return 'О нас'
    

class AboutImage(models.Model):
    image = models.ImageField(upload_to='about_us', blank=True)
    about = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='images')


class Offerta(models.Model):
    title = models.CharField(max_length=254, verbose_name='Загловок')
    descriptions = RichTextField(verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Публичная оферта'


    def __str__(self):
        return 'Публичная офферта'

class Help(models.Model):
    image = models.ImageField(upload_to='Help/')

    class Meta:
        verbose_name_plural = 'Help'

    def __str__(self):
        return 'Help'

class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    help = models.ForeignKey(Help, on_delete=models.CASCADE, related_name='help'
    
    )


LIST_CONTACT = (
    ('Number', 'Number'),
    ('Mail', 'Mail'),
    ('Telegram', 'Telegram'),
    ('WhatsApp', 'WhatsApp'),
    ('Instagram', 'Instagram'),
)


class Footer(models.Model):
    info = models.TextField(max_length=200, verbose_name='Информация')
    header_img = models.ImageField(upload_to='heder', blank=True, verbose_name='Логотип Футера')
    footer_img = models.ImageField(upload_to='footer', blank=True, verbose_name='Логотип Хедера')
    header_num = models.CharField(max_length=200, blank=True, verbose_name='Номер в хедере')
    mail = models.CharField(max_length=50, null=True, blank=True, verbose_name='Почта')
    instagram = models.CharField(max_length=100, blank=True, verbose_name='Instagram')
    num = PhoneNumberField(max_length=30, blank=True, verbose_name='Номер')
    whatsapp = models.CharField(max_length=30, blank=True, verbose_name='WhatsApp')
    telegram = models.CharField(max_length=30, blank=True, verbose_name='Telegram')

    def save(self, *args, **kwargs):
        if self.whatsapp and 'http' not in self.whatsapp: 
            self.whatsapp = f'http://wa.me/{self.whatsapp}/'
        if self.telegram and 'http' not in self.telegram:     
            self.telegram = f'https://t.me/{self.telegram}/' 
        if self.instagram and 'http' not in self.instagram:
            self.instagram = f'https://www.instagram.com/{self.instagram}/' 
        if self.mail and 'https' not in self.mail:
            self.mail = f'https://mail.doodle.com/{self.mail}/' 
        
           

        super(Footer, self).save(*args, **kwargs)



class Advantage(models.Model):
    image = models.ImageField(upload_to='advantage', blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'svg'])])
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
