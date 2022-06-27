from django.contrib import admin
from django.http import HttpRequest
from django.utils.safestring import mark_safe

from main.models import *

class ImageInline(admin.TabularInline):
    model = SliderImage
    max_num = 6 
    min_num = 1
    extra = 0

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Slider.objects.exists():
            retVal = False
        return retVal

class AboutImage(admin.TabularInline):
    model = AboutImage
    max_num = 3
    min_num = 1
    extra = 0

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutImage, ]

    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and AboutUs.objects.exists():
            retVal = False
        return retVal


class Question(admin.TabularInline):
    model = Question
    extra = 0


@admin.register(Offerta)
class OffertaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Offerta.objects.exists():
            retVal = False
        return retVal


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    inlines = [Question, ]

    def has_add_permission(self, request):
        # check if generally has add permissio``n
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Help.objects.exists():
            retVal = False
        return retVal



@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    


    def has_add_permission(self, request):
        # check if generally has add permissio``n
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Footer.objects.exists():
            retVal = False
        return retVal

    # def image_show(self, obj):
    #     if obj.image:
    #         return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
    #     return None 
    
    # image_show.__name__ = 'Изображение'

    def changelist_view(self, request: HttpRequest, extra_context=None):
        return super().changelist_view(request, extra_context=None)
    



# Register your models here.
admin.site.register(News)
admin.site.register(Advantage)
