from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from ShoeStore.utils import unique_slug_generator
from .models import Product


@receiver(pre_save, sender=Product)
def create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# @receiver(post_save, sender=Product)
# def update_price(sender, instance, created, *args, **kwargs):
#     if not created:
#         for child in instance.children.all():
#             if child.price_same_as_parent:
#                 child.price = instance.price
#                 child.save()
