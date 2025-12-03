from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event, RSVP, Review, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
        
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = "__all__"
        
           
class EventSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)
    class Meta:
        model = Event 
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "organizer")
    
      
    def create(self, validated_data):
        return super().create(validated_data)

class RSVPSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    
    class Meta:
        model = RSVP
        fields = "__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())

    class Meta:   
        model = Review
        fields = "__all__"
        read_only_fields = ("created_at",)
