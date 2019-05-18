from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import format_html

from product.models import Product


class ChildProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='children')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                blank=True)
    is_main = models.BooleanField(default=False,
                                  help_text='Should we display these details as \
                                  main product\'s details ? <br><b>Note : one \
                                  product should be set as main</b>')
    color = models.CharField(max_length=30)
    image = models.ImageField(upload_to="shoestore/")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Child Product"
        verbose_name_plural = "Child Products"
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.id} , {self.product.title} , {self.color}'

    def validate_unique(self, exclude=None):
        if ChildProduct.objects.exclude(pk=self.pk).filter(product__id=self.product.id,
                                                           color=self.color).exists():
            raise ValidationError('This color is already added for this product')

        if not ChildProduct.objects.exclude(pk=self.pk).filter(product__id =self.product.id,
                                           is_main=True).exists() and self.is_main==False:
            raise ValidationError('One child should be set as main')

        super(ChildProduct, self).validate_unique(exclude=exclude)

    def parent(self):
        return self.product.title

    def parent_id(self):
        return self.product.id

    def color_box(self):
        return format_html(
        f'<div style="background-color:{self.color};height:20px;width:20px;border:1px solid;"></div>'
        )
