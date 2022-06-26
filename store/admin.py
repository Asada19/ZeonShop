from django.contrib import admin
from django.utils.safestring import mark_safe
from store.models import Callback, Collection, Image, Product

# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image
    max_num = 12
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    readonly_fields=('stock', 'final_price',)
    fields = ('name', 'colection', 'articul', 'description', 'price', 'sales', 
                'final_price', 'size', 'stock', 'material', 'composition', 'favorite', 'new_prod', 'top_sales',)
    
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return None 
    
    image_show.__name__ = 'Изображение'

@admin.register(Callback)
class Callback(admin.ModelAdmin):
    list_display = ('name', 'phone', 'time', 'form', 'called', )
    readonly_fields = ['name', 'phone', 'time']
    

    def has_add_permission(self, request):
        # check if generally has add permissio``n
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal:
            retVal = False
        return retVal




admin.site.register(Collection)
