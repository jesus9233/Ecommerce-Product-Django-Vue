from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver

from .models import Cart


@receiver(m2m_changed, sender=Cart.products.through)
def set_subtotal(sender, instance, action, *args, **kwargs):
    if 'post' in action:
        products = instance.products.all()
        total = 0
        for product in products:
            total += product.child_product.price
        instance.subtotal = total
        instance.save()

@receiver(pre_save, sender=Cart)
def set_total(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = float(instance.subtotal) * float(1.08)
    else:
        instance.total = 0.00
