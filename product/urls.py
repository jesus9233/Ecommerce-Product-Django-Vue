from django.urls import path
from .views import ProductListAPIView, ProductByCategoryAPIView, latest_products, get_product, categories

app_name = "product"

urlpatterns = [
    path('', ProductListAPIView.as_view(), name="list"),
    path('categories/', categories, name='categories'),
    path('<str:category>/', ProductByCategoryAPIView.as_view(),
         name='product-categories'),
    path('detail/<slug:slug>/', get_product, name="detail"),
    path('latest/<int:limit>/', latest_products, name="latest-list")
]
