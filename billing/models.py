from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,
                                on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email}'
