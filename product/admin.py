from django.contrib import admin
from .models import Product, Category, Material, Brand, Tag


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['price', 'thumb']
    list_display = ['__str__', 'main_child']

    def get_queryset(self, request):
        return Product.objects.staff_all(request)


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
