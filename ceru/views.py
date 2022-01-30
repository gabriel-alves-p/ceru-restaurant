from django.shortcuts import render
from django.views import generic
from .models import Booking


class BookingDisplay(generic.ListView):
    """
    This class describes how to display
    bookings for the User to see.
    """
    model = Booking
    queryset = Booking.objects.order_by('-date')
    template_name = 'dashboard.html'
