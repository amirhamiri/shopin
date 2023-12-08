from django.contrib.auth.mixins import PermissionRequiredMixin

class PermissionsMixin(PermissionRequiredMixin):
    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_admin:
            return True

    def has_module_perms(self, app_label):
        if self.is_active and self.is_admin:
            return True