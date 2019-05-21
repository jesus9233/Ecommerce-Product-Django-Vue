from django.db import models
from django.conf import settings

from variants.models import Variant

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def get_or_new(self, request):
        created = False
        is_auth_user = request.user.is_authenticated
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id)
        if is_auth_user:
            user_qs = self.get_queryset().filter(user=request.user)
        if qs.exists():
            cart = qs.first()
            if is_auth_user and not cart.user:
                cart.user = request.user
                cart.save()
        elif is_auth_user and user_qs.exists():
            cart = user_qs.first()
        else:
            user_obj = None
            if request.user and is_auth_user:
                user_obj = request.user
            cart = self.get_queryset().create(user=user_obj)
            created = True
            request.session['cart_id'] = cart.id
        return cart, created


class Cart(models.Model):
    products = models.ManyToManyField(Variant, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    updated = models.DateTimeField(auto_now=True)
    objects = CartManager()

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['-updated']

    def __str__(self):
        return f'{self.id}'
