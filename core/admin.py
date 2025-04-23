from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User

# Register your models here.
class UserAdmin(DefaultUserAdmin):
    list_display = ('uuid', 'email', 'phone', 'first_name', 'last_name', 'created_at', 'updated_at')
    search_fields = ('email', 'phone', 'first_name', 'last_name')
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "phone",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

admin.site.register(User, UserAdmin)


