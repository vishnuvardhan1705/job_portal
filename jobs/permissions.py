from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsRecruiter(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'RECRUITER'


class IsJobOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.company.owner == request.user
