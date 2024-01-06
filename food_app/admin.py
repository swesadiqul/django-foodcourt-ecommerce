from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Category)


class ImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1  # Number of empty forms to display for adding new images

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'comment', 'created_at')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass