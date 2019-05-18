from django.urls import path
from .views import get_variant, get_variantdetails

app_name = 'variants'

urlpatterns = [
    path('details/<str:ids>/', get_variantdetails, name='details'),
    path('<int:id>/<color>/', get_variant, name='list'),
]
