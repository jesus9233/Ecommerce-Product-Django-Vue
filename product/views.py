from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status

from childproduct.serializers import ChildProductRetrieveSerializer
from .serializers import ProductSerializer, ProductRetrieveSerializer
from .models import Product, Category
from .paginations import MyPagination


class ProductListAPIView(ListAPIView):
    queryset = Product.items.all()
    serializer_class = ProductSerializer
    pagination_class = MyPagination
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('search')
        if query:
            return Product.items.search(query)
        return Product.items.all()


class ProductByCategoryAPIView(ListAPIView):
    queryset = Product.items.all()
    serializer_class = ProductSerializer
    pagination_class = MyPagination
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        category = self.kwargs.get('category')
        if category:
            return Product.items.filter(category__name__iexact=category)
        return Response(status=status.status.HTTP_404_NOT_FOUND)


@api_view()
@permission_classes([AllowAny])
def latest_products(request, limit):
    products_data = Product.items.limit(limit)
    serializer = ProductSerializer(products_data, many=True)
    return Response(serializer.data)


@api_view()
@permission_classes([AllowAny])
def get_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    childproducts = product.children.all()
    serialized_product = ProductRetrieveSerializer(product)
    serialized_childproducts = ChildProductRetrieveSerializer(childproducts,
                                                              many=True)
    serializer = {
        'product': serialized_product.data,
        'children': serialized_childproducts.data,
        }
    return Response(serializer)


@api_view()
@permission_classes([AllowAny])
def categories(request):
    categories = Category.objects.all().exclude(Q(name='unspecified')
                                                | Q(name='other')
                                                | Q(products=None))
    data = [category.name for category in categories]
    return Response(data)
