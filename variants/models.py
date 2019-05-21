from django.db import models
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from childproduct.models import ChildProduct


class VariantManager(models.Manager):
    def get_details(self, ids):
        details = []
        for id in ids:
            variant = get_object_or_404(Variant, id=id)
            child = variant.child_product
            thumb = child.image.url
            name = child.product.title
            slug = child.product.slug
            price = child.price
            id = variant.id
            size = variant.size
            details.append({
                'id': id,
                'thumb': thumb,
                'name': name,
                'slug': slug,
                'price': price,
                'size': size,
                })
        return details


size_chocies = (
    ('5', '5 IN'),
    ('6', '6 IN'),
    ('7', '7 IN'),
    ('8', '8 IN'),
    ('9', '9 IN'),
    ('10', '10 IN'),
    ('11', '11 IN'),
)


class Variant(models.Model):
    child_product = models.ForeignKey(ChildProduct, on_delete=models.CASCADE,
                                      related_name='variants')
    size = models.CharField(max_length=2, choices=size_chocies)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = VariantManager()

    class Meta:
        verbose_name = "Variant"
        verbose_name_plural = "Variants"
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.id}'

    def validate_unique(self, exclude=None):
        if Variant.objects.exclude(pk=self.pk).filter(child_product__id=self.child_product.id,
                                                      child_product__color=self.child_product.color,
                                                      size=self.size).exists():
            raise ValidationError("This size is already added for this produc\
            t's color")
        super(Variant, self).validate_unique(exclude=exclude)

    def parent(self):
        return self.child_product.product.title

    def parent_id(self):
        return self.child_product.product.id

    def child_product_id(self):
        return self.child_product.id

    def color_box(self):
        return self.child_product.color_box()
