from rest_framework import permissions

class IsActiveEmployee(permissions.BasePermission):
    """Позволяет доступ только активным сотрудникам."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active
