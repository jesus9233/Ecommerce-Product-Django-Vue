from rest_framework import serializers
# from rest_framework.serializers import SerializerMethodField
from .models import ChildProduct


class ChildProductRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildProduct
        fields = '__all__'
