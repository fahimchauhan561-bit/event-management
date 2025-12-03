from rest_framework import permissions

class IsOrganizerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(obj, "organizer") and obj.organizer == request.user
    
    
class IsInvitedOrPublic(permissions.BasePermission):
    """
    Allow access if the event is public.
    If event is private → only organizer, staff, or invited users can view it.
    """

    def has_object_permission(self, request, view, obj):

        # If public → allow everyone
        if obj.is_public:
            return True

        # Organizer can always access
        if obj.organizer == request.user:
            return True

        # Staff / admin can always access
        if request.user.is_staff:
            return True

        # Invited users can access
        if hasattr(obj, "invited_users") and request.user in obj.invited_users.all():
            return True

        # Otherwise deny
        return False
