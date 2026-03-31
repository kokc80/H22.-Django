from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Product
admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "cost", "category")
    list_filter = ("category",)
    search_fields = ("name", "descr",)
