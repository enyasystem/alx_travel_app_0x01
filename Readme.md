# 🏠 ALX Travel App 0x00

Welcome to the ALX Travel App 0x00 project! This Django app demonstrates database modeling, API serialization, and data seeding for a travel booking platform.

## 🚀 Features
- Listings for properties (apartments, houses, etc.)
- Bookings for guests with date ranges
- Reviews for listings
- API serialization for Listings and Bookings
- Database seeder for quick sample data

## 🛠️ Tech Stack
- Python 3.x 🐍
- Django 🌐
- Django REST Framework 🛡️
- SQLite (easy to switch to PostgreSQL/MySQL)

## 📦 How to Run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py makemigrations && python manage.py migrate`
4. Seed the database: `python manage.py seed`
5. Start the server: `python manage.py runserver`

## 🧑‍💻 API Endpoints
- `/listings/` : List and manage property listings
- `/bookings/` : List and manage bookings

## 📝 Example Usage
- Add a new listing
- Book a property for a guest
- Leave a review for a listing

## 📚 Learning Outcomes
- Model relationships in Django
- Serialize data for APIs
- Use management commands for seeding

## 🤝 Contributing
PRs are welcome! Please open an issue or discussion for major changes.

Happy travels and coding! ✈️🚀
