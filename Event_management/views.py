from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Event, RSVP, Review
from .serializers import EventSerializer, RSVPSerializer, ReviewSerializer
from .permissions import IsOrganizerOrReadOnly, IsInvitedOrPublic

from rest_framework.pagination import PageNumberPagination


# Simple Pagination
class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"


# ------------- EVENT API ----------------

class EventListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        return Event.objects.filter(is_public=True).order_by('-start_time')

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]     # Only auth users can POST
        return [AllowAny()]                # Anyone can GET

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)



class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOrganizerOrReadOnly, IsInvitedOrPublic]



# ------------- RSVP API ----------------

class RSVPCreateAPIView(generics.CreateAPIView):
    serializer_class = RSVPSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        event = get_object_or_404(Event, id=self.kwargs["event_id"])
        serializer.save(user=self.request.user, event=event)


class RSVPUpdateAPIView(generics.UpdateAPIView):
    serializer_class = RSVPSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        event = get_object_or_404(Event, id=self.kwargs["event_id"])
        return get_object_or_404(RSVP, event=event, user__id=self.kwargs["user_id"])



# ------------- REVIEW API ----------------

class ReviewListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]      # Only logged-in users can review
        return [AllowAny()]                 # Anyone can GET reviews

    def get_queryset(self):
        return Review.objects.filter(event_id=self.kwargs["event_id"]).order_by('-created_at')

    def perform_create(self, serializer):
        event = get_object_or_404(Event, id=self.kwargs["event_id"])
        serializer.save(user=self.request.user, event=event)
