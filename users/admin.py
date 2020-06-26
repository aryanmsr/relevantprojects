from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_filter = ['is_company']
    list_display = ['company_name', 'username', 'is_company', 'is_verified']
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'is_verified',
                ),
            },
        ),
    )
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
