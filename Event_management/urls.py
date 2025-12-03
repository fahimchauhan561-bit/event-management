# Event_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Events
    path("events/", views.EventListCreateAPIView.as_view(), name="events-list-create"),
    path("events/<int:pk>/", views.EventDetailAPIView.as_view(), name="event-detail"),

    # RSVP
    path("events/<int:event_id>/rsvp/", views.RSVPCreateAPIView.as_view(), name="rsvp-create"),
    path("events/<int:event_id>/rsvp/<int:user_id>/", views.RSVPUpdateAPIView.as_view(), name="rsvp-update"),

    # Reviews
    path("events/<int:event_id>/reviews/", views.ReviewListCreateAPIView.as_view(), name="review-list-create"),
]
