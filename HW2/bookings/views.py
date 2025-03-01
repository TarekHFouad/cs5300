# bookings/views.py
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# API viewsets using Django REST Framework

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Template views

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(is_booked=False)
    if request.method == 'POST':
        if seats.exists():
            seat = seats.first()
            # In a real app, ensure that request.user is authenticated
            booking = Booking.objects.create(movie=movie, seat=seat, user=request.user)
            seat.is_booked = True
            seat.save()
            return redirect('booking_history')
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
