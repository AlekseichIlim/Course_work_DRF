from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    """Определяет, является ли пользователь владельцем объекта"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
