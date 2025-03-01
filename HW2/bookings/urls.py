# bookings/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, seat_booking, booking_history

router = DefaultRouter()
router.register(r'api/movies', MovieViewSet)
router.register(r'api/seats', SeatViewSet)
router.register(r'api/bookings', BookingViewSet)

urlpatterns = [
    # API endpoints
    path('', include(router.urls)),
    # Template views
    path('movies/', movie_list, name='movie_list'),
    path('book_seat/<int:movie_id>/', seat_booking, name='book_seat'),
    path('booking_history/', booking_history, name='booking_history'),
]
