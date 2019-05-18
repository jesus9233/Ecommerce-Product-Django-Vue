from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import Product
# from .models import Color


class ProductSerializer(serializers.ModelSerializer):
    # image = SerializerMethodField()
    # size = SerializerMethodField()
    # brand = SerializerMethodField()
    # category = SerializerMethodField()
    # material_type = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title','slug','price','thumb']
    #
    # def get_color(self, obj):
    #     try:
    #         color = [x.value for x in obj.color.all()]
    #     except Exception as e:
    #         color = None
    #     return color
    #
    # def get_size(self, obj):
    #     try:
    #         size = [x.number for x in obj.size.all()]
    #     except Exception as e:
    #         size = None
    #     return size
    #
    # def get_category(self, obj):
    #     try:
    #         category = obj.category.name
    #     except Exception as e:
    #         category = None
    #     return category
    #
    # def get_material_type(self, obj):
    #     try:
    #         material_type = obj.material_type.name
    #     except Exception as e:
    #         material_type = None
    #     return material_type
    #
    # def get_brand(self, obj):
    #     try:
    #         brand = obj.brand.name
    #     except Exception as e:
    #         brand = None
    #     return brand

class ProductRetrieveSerializer(serializers.ModelSerializer):
    brand = SerializerMethodField()
    category = SerializerMethodField()
    material_type = SerializerMethodField()


    class Meta:
        model = Product
        fields = '__all__'

    def get_category(self, obj):
        try:
            category = obj.category.name
        except Exception as e:
            category = None
        return category

    def get_material_type(self, obj):
        try:
            material_type = obj.material_type.name
        except Exception as e:
            material_type = None
        return material_type

    def get_brand(self, obj):
        try:
            brand = obj.brand.name
        except Exception as e:
            brand = None
        return brand
