from django.contrib import admin

from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Настройки администратора для пользователя"""
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser',)
    list_filter = ('is_active',)
    readonly_fields = ('last_login', 'date_joined')

    fieldsets = (
        ('Общая информация', {
            'fields': ('username', ('last_login', 'date_joined'))
        }),
        ('Контактная информация', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Статусная информация', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Права доступа', {
            'fields': ('groups', 'user_permissions')
        }),
    )