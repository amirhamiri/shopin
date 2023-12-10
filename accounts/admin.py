from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.contrib.auth.models import Group


class UserAdmin(UserAdmin):
    list_display = ('phone','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('phone','is_admin', 'password')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'),
        }),

    )
    search_fields = ('phone',)
    ordering = ('-id',)
    filter_horizontal = ()


admin.site.register(models.User, UserAdmin)
admin.site.unregister(Group)
