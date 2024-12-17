from rest_framework.permissions import BasePermission

class IsLibrarian(BasePermission):
    """
    Custom permission to allow only librarian users to access certain views.
    """

    def has_permission(self, request, view):
        # Ensure user is authenticated and has 'role' attribute
        if not request.user or not hasattr(request.user, 'role'):
            return False

        # Check if the user has the 'librarian' role
        if request.user.role == 'librarian':
            return True
        
        return False
