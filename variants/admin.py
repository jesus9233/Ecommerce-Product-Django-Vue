from django.contrib import admin
from .models import Variant

class VariantAdmin(admin.ModelAdmin):
    list_display = ('id','size','child_product_id','parent_id','parent','color_box')

admin.site.register(Variant, VariantAdmin)
