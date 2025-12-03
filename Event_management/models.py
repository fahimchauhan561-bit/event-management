from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    #profile_picture = models.ImageField(
        #upload_to = 'profile_pictures/'
    #)
    def __str__(self):
        return f"{self.user}  {self.full_name}  {self.bio} {self.location} "
    

class Event(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField(blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} {self.description} {self.organizer} {self.location} {self.start_time} {self.end_time} {self.is_public} {self.created_at} {self.updated_at}"


class RSVP(models.Model):
    STATUS_CHOICES = [
        ('Going', 'Going'),
        ('Maybe', 'Maybe'),
        ('Not Going','Not Going'),
        
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    def __str__(self):
        return f"{self.user.username} -> {self.event.title} ({self.status})"
    
    
class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"Review by {self.user.username} on {self.event.title}"