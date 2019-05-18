from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import ChildProduct
from product.models import Product

#
# @receiver(pre_save, sender = ChildProduct)
# def check_main(sender, instance, *args, **kwargs):
#     if not ChildProduct.objects.filter(product__id=instance.product.id,
#                                        is_main=True).exists():
#         instance.is_main=True


@receiver(post_save, sender = ChildProduct)
def set_main(sender, instance, created, *args, **kwargs):
    if instance.is_main:
        qs = ChildProduct.objects.exclude(pk=instance.pk).filter(product__id = instance.product.id,
                                                                 is_main=True)
        if qs.exists() and instance.is_main == True:
            qs.update(is_main=False)

        product = Product.objects.get(id=instance.product.id)
        product.price = instance.price
        product.thumb = instance.image
        product.save()
