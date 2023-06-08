from django.contrib import admin

from store.products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity')
    fields = ('name', 'description', 'price', 'quantity', 'image', 'category')
    search_fields = ('name',)
    readonly_fields = ('description',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0
