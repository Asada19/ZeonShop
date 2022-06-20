from django.contrib import admin

from main.models import News, SliderImage, Slider

class ImageInline(admin.TabularInline):
    model = SliderImage
    max_num = 6 
    min_num = 1
    extra = 0


class SliderAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


# Register your models here.
admin.site.register(News)
admin.site.register(Slider, SliderAdmin)
