from django.shortcuts import render
from django.views import generic
from .models import Booking


class IndexView(generic.ListView):
    """
    This class is the view for the
    'home' page or 'index.html'.
    """
    model = Booking
    queryset = Booking
    template_name = 'index.html'


class BookingDisplay(generic.ListView):
    """
    This class describes how to display
    bookings for the User to see.
    """
    model = Booking
    queryset = Booking.objects.order_by('-date')
    template_name = 'dashboard.html'
