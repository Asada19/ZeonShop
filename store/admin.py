from django.contrib import admin

from store.models import Collection, Image, Product

# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image
    max_num = 12
    min_num = 1
    extra = 0

    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    readonly_fields=('stock', 'final_price', )
    fields = ('name', 'colection', 'articul', 'description', 'price', 'sales', 
                'final_price', 'size', 'stock', 'material', 'composition','favorite', 'new_prod', 'top_sales', )
    
    



admin.site.register(Product, ProductAdmin)
admin.site.register(Collection)
