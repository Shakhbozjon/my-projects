from django.contrib import admin
from .models import Category, Goods

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['name', 'price']
    date_hierarchy = 'publish_time'
    search_fields = ['name']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

