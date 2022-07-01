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
        # check if generally has add permissio``n
        obj6 = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if obj6:
            obj6 = False
        return obj6


class AboutImage(admin.TabularInline):
    model = AboutImage
    max_num = 3
    min_num = 1
    extra = 0


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutImage, ]

    def has_add_permission(self, request):
        # check if generally has add permissio``n
        obj5 = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if obj5:
            obj5 = False
        return obj5


class Question(admin.TabularInline):
    model = Question
    extra = 0


@admin.register(Offerta)
class OffertaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permissio``n
        obj4 = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if obj4:
            obj4 = False
        return obj4


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    inlines = [Question, ]

    def has_add_permission(self, request):
        # check if generally has add permissio``n
        obj2 = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if obj2:
            obj2 = False
        return obj2


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permissio``n
        obj3 = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if obj3:
            obj3 = False
        return obj3

    def changelist_view(self, request: HttpRequest, extra_context=None):
        return super().changelist_view(request, extra_context=None)
