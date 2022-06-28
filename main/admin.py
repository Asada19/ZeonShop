from django.contrib import admin
from django.http import HttpRequest
from main.models import *

admin.site.register(News)
admin.site.register(Advantage)


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
        obj = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if obj and Slider.objects.exists():
            obj = False
        return obj


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
        obj = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if obj and Slider.objects.exists():
            obj = False
        return obj


class Question(admin.TabularInline):
    model = Question
    extra = 0


@admin.register(Offerta)
class OffertaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permission
        obj = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if obj and Slider.objects.exists():
            obj = False
        return obj


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    inlines = [Question, ]

    def has_add_permission(self, request):
        # check if generally has add permission
        obj = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if obj and Slider.objects.exists():
            obj = False
        return obj


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permission
        obj = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if obj and Slider.objects.exists():
            obj = False
        return obj

    def changelist_view(self, request: HttpRequest, extra_context=None):
        return super().changelist_view(request, extra_context=None)
