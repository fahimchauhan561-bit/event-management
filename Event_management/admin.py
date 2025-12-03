from django.contrib import admin
from .models import UserProfile, Event, RSVP, Review

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'bio', 'location') #'profile_picture')
    
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'organizer', 'location', 'start_time', 'end_time', 'is_public', 'created_at', 'updated_at')
    
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Event,EventAdmin)


class RSVPAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'status')
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'rating', 'created_at')
    
admin.site.register(RSVP,RSVPAdmin)
admin.site.register(Review,ReviewAdmin)

