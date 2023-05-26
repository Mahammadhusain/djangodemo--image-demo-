from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import gettext as _
# Create your models here.
class LinksUserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        values = [email]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError("The {} value must be set".format(field_name))

        email = self.normalize_email(email)
        user = self.model(username=email,email=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_user(self,username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email,username, password, **extra_fields)

    def create_superuser(self,username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email,username, password, **extra_fields)


class LinksUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField( unique=True)
    username = models.CharField(unique=True, max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    # EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['email']

    objects = LinksUserManager()
    def __str__(self):
        return self.email
