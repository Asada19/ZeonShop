from django.contrib import admin
from store.models import Callback, Collection, Image, Product, Cart, Order, CartItem


class ImageInline(admin.TabularInline):
    model = Image
    max_num = 12
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    readonly_fields = ('stock', 'final_price',)
    list_display = ('name', 'colection', 'final_price', 'size', 'stock', 'favorite', 'new_prod', 'top_sales')
    fields = ('name', 'colection', 'articul', 'description', 'price', 'sales', 
              'final_price', 'size', 'stock', 'material', 'composition', 'favorite', 'new_prod', 'top_sales',)
    

@admin.register(Callback)
class Callback(admin.ModelAdmin):
    list_display = ('name', 'phone', 'time', 'form', 'called', )
    readonly_fields = ['name', 'phone', 'time']

    def has_add_permission(self, request):
        # check if generally has add permissio``n
        obj1 = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if obj1:
            onj1 = False
        return obj1


class DetailInline(admin.TabularInline):
    model = CartItem
    extra = 0
    # readonly_fields = ('price', 'quantity', 'sum', 'sum_quantity', 'discounts', 'total', )


@admin.register(Order)
class Order(admin.ModelAdmin):
    inlines = [DetailInline, ]
    list_display = ('name', 'num', 'city', 'date_order', 'status', )


admin.site.register(Collection)
# admin.site.register(Cart)
admin.site.register(CartItem)
# admin.site.register(Order)
