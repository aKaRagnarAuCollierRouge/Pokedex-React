from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,TypeAccount

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'birthday', 'date_joined', 'is_active', 'is_staff', 'type_account', 'subscription_start_date', 'subscription_end_date')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'birthday')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Subscription', {'fields': ('type_account', 'subscription_start_date', 'subscription_end_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TypeAccount)
