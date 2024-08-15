from django.contrib.admin import ModelAdmin, register, StackedInline

from .models import Category, Product, ProductImage



class ProductImageSteckedInline(StackedInline):
    model = ProductImage
    fields = ('product', 'image')


@register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = ProductImageSteckedInline,
    list_display = 'name', 'category', 'price', 'quantity'


@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass