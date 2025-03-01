# bookings/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.movie = Movie.objects.create(
            title='Test Movie',
            description='A test movie.',
            release_date=date.today(),
            duration=120
        )
        self.seat = Seat.objects.create(seat_number='A1')

    def test_create_booking(self):
        booking = Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)
        self.assertEqual(str(booking), f"{self.user.username} booked {self.seat} for {self.movie}")
