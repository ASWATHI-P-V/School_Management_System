from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUserOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to have write access.
    """
    def has_permission(self, request, view):
        # Allow read-only access for any user
        if request.method in SAFE_METHODS:
            return True
        
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Only allow write access for admin users
            return request.user.role == 'admin'
        
        # Deny access for unauthenticated users
        return False

