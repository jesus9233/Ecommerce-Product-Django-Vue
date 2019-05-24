from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import Product
# from .models import Color


class ProductSerializer(serializers.ModelSerializer):
    colors = SerializerMethodField()
    sizes = SerializerMethodField()
    brand = SerializerMethodField()
    # category = SerializerMethodField()
    # material_type = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'price', 'brand', 'thumb', 'colors',
                  'sizes']
    #
    # def get_color(self, obj):
    #     try:
    #         color = [x.value for x in obj.color.all()]
    #     except Exception as e:
    #         color = None
    #     return color
    #

    def get_colors(self, obj):
        try:
            colors = [x.color for x in obj.children.all()]
        except Exception as e:
            colors = None
            print(e)
        return colors

    def get_sizes(self, obj):
        try:
            sizes = None
            sizes = [variant.size for children in obj.children.all()
                     for variant in children.variants.all()]
            sizes = list(set(sizes))
            # print(sizes)
            sizes.sort(reverse=True)
        except Exception as e:
            sizes = None
            print(e)
        return sizes
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

    def get_brand(self, obj):
        try:
            brand = obj.brand.name
        except Exception as e:
            brand = None
            print(e)
        return brand


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
