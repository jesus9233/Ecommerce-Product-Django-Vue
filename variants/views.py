from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Variant
from .serializers import VariantSerializer


@api_view()
@permission_classes([AllowAny])
def get_variant(request, id, color):
    color = '#'+color
    variants = Variant.objects.filter(child_product__id=id,
                                      child_product__color=color)
    serializer = VariantSerializer(variants, many=True)
    return Response(serializer.data)


@api_view()
@permission_classes([AllowAny])
def get_variantdetails(request, ids):
    details = Variant.objects.get_details(ids)
    return Response(details)
