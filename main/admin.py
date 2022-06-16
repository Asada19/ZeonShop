from django.contrib import admin

from main.models import News, Image, Slider

class ImageInline(admin.TabularInline):
    model = Image
    max_num = 6 
    min_num = 1
    extra = 0


class SliderAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


# Register your models here.
admin.site.register(News)
admin.site.register(Slider, SliderAdmin)
