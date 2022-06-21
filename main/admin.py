from django.contrib import admin

from main.models import AboutUs, AboutImage, Help, News, Offerta, Question, SliderImage, Slider

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



# Register your models here.
admin.site.register(News)

