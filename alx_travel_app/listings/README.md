# 🏠 Listings App

The Listings app is a core component of the ALX Travel App that handles property listings, bookings, and reviews. It provides a RESTful API for managing travel accommodations and reservations.

## 📦 Models

### Listing
- `title`: Name/title of the property
- `description`: Detailed description of the property
- `price`: Cost per night/stay
- `created_at`: Timestamp of listing creation

### Booking
- `listing`: Foreign key to the associated Listing
- `guest_name`: Name of the guest making the booking
- `start_date`: Check-in date
- `end_date`: Check-out date
- `created_at`: Timestamp of booking creation

### Review
- `listing`: Foreign key to the reviewed Listing
- `reviewer_name`: Name of the person writing the review
- `rating`: Numerical rating (positive integer)
- `comment`: Text feedback
- `created_at`: Timestamp of review creation

## 🌐 API Endpoints

The app uses Django REST Framework's ViewSets to provide CRUD operations:

### Listings
- `GET /api/listings/`: List all properties
- `POST /api/listings/`: Create a new listing
- `GET /api/listings/{id}/`: Retrieve a specific listing
- `PUT/PATCH /api/listings/{id}/`: Update a listing
- `DELETE /api/listings/{id}/`: Remove a listing

### Bookings
- `GET /api/bookings/`: List all bookings
- `POST /api/bookings/`: Create a new booking
- `GET /api/bookings/{id}/`: Retrieve a specific booking
- `PUT/PATCH /api/bookings/{id}/`: Update a booking
- `DELETE /api/bookings/{id}/`: Cancel a booking

## 🌱 Data Seeding

The app includes a management command to seed the database with sample data:

```bash
python manage.py seed
```

This creates sample listings, bookings, and reviews for testing purposes.

## 📚 Documentation

API documentation is available through Swagger UI and ReDoc:
- Swagger: `/api/docs/swagger/`
- ReDoc: `/api/docs/redoc/`