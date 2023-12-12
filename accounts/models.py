from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser):
    phone = models.CharField(_("Phone number"), unique=True, max_length=11)
    is_admin = models.BooleanField(_("Is admin"), default=False)
    is_active = models.BooleanField(_("Is active"), default=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.phone

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_admin:
            return True

    def has_module_perms(self, app_label):
        if self.is_active and self.is_admin:
            return True
