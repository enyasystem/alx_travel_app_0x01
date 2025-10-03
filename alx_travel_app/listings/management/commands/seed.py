from django.core.management.base import BaseCommand
from alx_travel_app.listings.models import Listing, Booking, Review
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews.'

    def handle(self, *args, **kwargs):
        # Create Listings
        listing1 = Listing.objects.create(title='Cozy Apartment', description='A nice place to stay.', price=100.00)
        listing2 = Listing.objects.create(title='Beach House', description='Enjoy the sea breeze.', price=250.00)

        # Create Bookings
        Booking.objects.create(listing=listing1, guest_name='Alice', start_date=date.today(), end_date=date.today() + timedelta(days=2))
        Booking.objects.create(listing=listing2, guest_name='Bob', start_date=date.today(), end_date=date.today() + timedelta(days=5))

        # Create Reviews
        Review.objects.create(listing=listing1, reviewer_name='Charlie', rating=5, comment='Loved it!')
        Review.objects.create(listing=listing2, reviewer_name='Dana', rating=4, comment='Great view!')

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
