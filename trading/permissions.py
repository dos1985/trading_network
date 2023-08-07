from rest_framework import permissions
from core.managers import UserRoles


class IsActiveEmployee(permissions.BasePermission):
    """Позволяет доступ только активным сотрудникам."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Разрешение, позволяющее только владельцам объекта редактировать или удалять его."""
    def has_object_permission(self, request, view, obj):
        # Чтение разрешено для любого запроса,
        # поэтому мы всегда будем разрешать запросы GET, HEAD или OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Запись разрешена только владельцу объекта.
        return obj.user == request.user


class IsAdminUser(permissions.BasePermission):
    """Разрешение, позволяющее только администраторам создавать заводы."""
    def has_permission(self, request, view):
        return request.user.role == UserRoles.ADMIN