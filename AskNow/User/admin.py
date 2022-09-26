from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from User.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'created_at',
                    'updated_at', 'is_active', 'is_staff')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permission', {'fields': ('is_staff', 'is_active', 'is_superuser')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')
        }
        ),
    )
    search_fields = ('email', 'username',)
    ordering = ('created_at',)


admin.site.register(User, CustomUserAdmin)
