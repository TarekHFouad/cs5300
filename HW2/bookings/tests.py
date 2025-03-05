# bookings/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title='Test Movie',
            description='A test movie.',
            release_date=date.today(),
            duration=120
        )

    def test_movie_str(self):
        self.assertEqual(str(self.movie), 'Test Movie')

class SeatModelTest(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_number='A1', is_booked=False)

    def test_seat_str(self):
        self.assertEqual(str(self.seat), 'A1')

class BookingViewTest(TestCase):
    def setUp(self):
        # Create a user for login
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create a movie and a seat for booking
        self.movie = Movie.objects.create(
            title='Test Movie',
            description='A test movie.',
            release_date=date.today(),
            duration=120
        )
        self.seat = Seat.objects.create(seat_number='A1', is_booked=False)
        # Create a test client
        self.client = Client()


class MovieAPI_Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(
            title='API Test Movie',
            description='Testing the API.',
            release_date=date.today(),
            duration=100
        )

    def test_movie_api_get(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
        # Optionally, check that the response contains your movie title
        self.assertContains(response, 'API Test Movie')
