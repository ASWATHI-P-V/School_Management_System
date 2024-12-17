from rest_framework.permissions import BasePermission

class IsOfficeStaff(BasePermission):
    def has_permission(self, request, view):
        # Ensure user is authenticated and has 'role' attribute
        if not request.user or not hasattr(request.user, 'role'):
            return False

        # Check if the user has the 'officestaff' role
        if request.user.role == 'officestaff':
            return True
        
        return False

