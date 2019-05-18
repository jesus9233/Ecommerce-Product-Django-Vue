from django.db import models
from django.db.models import Q
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Material Type"
        verbose_name_plural = "Material Types"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=120, unique = True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def limit(self,limit):
        count = limit
        if count > 0:
            return self.get_queryset().all()[:count]
        else:
            return self.get_queryset().all()

    def search(self, query):
        query_list = query.split(' ')
        lookups = (Q(title__icontains=query) | Q(description__icontains=query) |
        Q(slug__icontains=query) | Q(tags__name__in = query_list))
        return self.get_queryset().filter(lookups).distinct()

gender_choices = (
    ('male','Male'),
    ('female','Female'),
)

def get_unspecified_brand():
    return Brand.objects.get_or_create(name="unspecified")[0]

def get_unspecified_material():
    return Material.objects.get_or_create(name="unspecified")[0]

def get_unspecified_category():
    return Category.objects.get_or_create(name="unspecified")[0]


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    gender = models.CharField(max_length=6, choices=gender_choices)
    brand = models.ForeignKey(Brand, on_delete = models.SET(get_unspecified_brand))
    category = models.ForeignKey(Category,  related_name='products',
                                on_delete = models.SET(get_unspecified_category))
    material_type = models.ForeignKey(Material, on_delete = models.SET(get_unspecified_material))
    tags = models.ManyToManyField(Tag, blank=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                blank=True,help_text='Derived from main child')
    thumb = models.ImageField(upload_to="shoestore/", null=True, blank=True,
                              help_text='Derived from main child')
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    objects = ProductManager()


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-timestamp']

    def __str__(self):
        return f'id : {self.id}, title : {self.title}'

    def get_absolute_url(self, **kwargs):
        return reverse('product:detail', kwargs={'slug': self.slug})

    def main_child(self):
        return self.children.filter(is_main=True).first()
