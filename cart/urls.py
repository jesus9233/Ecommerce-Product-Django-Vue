from django.urls import path
from .views import cart_home, cart_edit

app_name = 'cart'

urlpatterns = [
    path('', cart_home, name='view'),
    path('edit/<int:product_id>/', cart_edit, name='edit')
]
