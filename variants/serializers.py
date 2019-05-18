from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import Variant

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'
