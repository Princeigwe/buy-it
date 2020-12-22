from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'price', 'available', 'description', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
