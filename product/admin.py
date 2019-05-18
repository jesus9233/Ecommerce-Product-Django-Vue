from django.contrib import admin
from .models import Product, Category, Material, Brand, Tag

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['price','thumb']
    list_display = ['__str__','main_child']

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
