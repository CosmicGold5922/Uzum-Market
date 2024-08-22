from django.contrib.admin import ModelAdmin, register, StackedInline

from .models import Category, Product, ProductImage, ProductColor



class ProductImageSteckedInline(StackedInline):
    model = ProductImage
    fields = ('Product', 'image')


class ProductColorSteckedInline(StackedInline):
    model = ProductColor
    fields = ('Product', 'name')


@register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = ProductImageSteckedInline, ProductColorSteckedInline
    list_display = 'name', 'category', 'price', 'quantity'


@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass