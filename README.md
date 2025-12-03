📌 Event Management API — Assignment

username and password for admin 
username :- fahim   
password  :- 123@abc
This project is a Django REST Framework (DRF) based API for managing events, RSVPs, and reviews.
It includes authentication, permissions, and clean REST API design as required in the assignment.

🚀 Features
✔ User Profile

Extends Django User model

Fields: full_name, bio, location, profile_picture

✔ Events

Create, list, update, delete events

Only organizer can modify their events

Private events restricted

Timestamps auto-tracked

✔ RSVP

Users can respond with:

Going

Maybe

Not Going

✔ Event Reviews

Users can leave:

Rating (integer)

Comment

🔐 Authentication (JWT)

This project uses JSON Web Tokens (JWT).

Endpoint	Type	Description
/api/token/	POST	Get access + refresh tokens
/api/token/refresh/	POST	Refresh access token

Usage in headers:

Authorization: Bearer <access_token>

📡 API Endpoints
🎉 Event API
Method	Endpoint	Description
POST	/api/events/	Create event (auth required)
GET	/api/events/	List all public events (pagination)
GET	/api/events/<id>/	Get event details
PUT	/api/events/<id>/	Update event (only organizer)
DELETE	/api/events/<id>/	Delete event (only organizer)
✋ RSVP API
Method	Endpoint	Description
POST	/api/events/<event_id>/rsvp/	RSVP to event
PATCH	/api/events/<event_id>/rsvp/<user_id>/	Update RSVP
⭐ Review API
Method	Endpoint	Description
POST	/api/events/<event_id>/reviews/	Add review
GET	/api/events/<event_id>/reviews/	List reviews
🔒 Permissions
✔ IsOrganizerOrReadOnly

Anyone can view

Only organizer can edit/delete

✔ Private Event Restriction

Private events require:

Organizer

Staff

(Future: invited users)

▶️ Setup Instructions
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Apply migrations
python manage.py migrate

3️⃣ Run server
python manage.py runserver

4️⃣ Create superuser
python manage.py createsuperuser

📁 Project Structure
project/
│── website/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│── Event_management/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│── db.sqlite3
│── manage.py
│── README.md

🎯 Conclusion

This project fulfills all assignment requirements:
✔ Models
✔ Serializers
✔ API Views
✔ Permissions
✔ JWT Authentication
✔ Pagination
✔ Clean REST structure

Fahim Chauhan

