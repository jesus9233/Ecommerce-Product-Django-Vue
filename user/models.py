from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'auth_user'
        app_label = 'user'


email = User._meta.get_field('email')
email._unique = True
email.blank = False
