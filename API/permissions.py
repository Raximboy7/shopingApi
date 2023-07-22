from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Sadece GET, HEAD veya OPTIONS taleplerine izin ver
        if request.method in permissions.SAFE_METHODS:
            return True

        # Sadece admin kullanıcısına izin ver
        return request.user and request.user.is_staff
