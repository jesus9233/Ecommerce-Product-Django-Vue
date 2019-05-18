from django.contrib import admin
from .models import ChildProduct
from .forms import ChildProductForm


class ChildProductAdmin(admin.ModelAdmin):
    form = ChildProductForm
    list_display = ('id','color_box','parent_id','parent')


admin.site.register(ChildProduct, ChildProductAdmin)
