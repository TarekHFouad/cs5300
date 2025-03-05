from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, seat_booking, booking_history

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # Template view for the home page
    path('', movie_list, name='movie_list'),
    # API endpoints will now be at /api/movies/, /api/seats/, /api/bookings/
    path('api/', include(router.urls)),
    path('movies/', movie_list, name='movie_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('book_seat/<int:movie_id>/', seat_booking, name='book_seat'),
    path('booking_history/', booking_history, name='booking_history'),
]
