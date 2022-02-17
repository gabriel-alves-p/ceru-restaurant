from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from .models import Booking


class HomeTemplateView(TemplateView):
    """
    Home page template view.
    """
    template_name = 'index.html'


class BookingView(TemplateView):
    """
    Booking form page template view.
    """
    template_name = 'booking_form.html'
    model = Booking


class EditBookingView(TemplateView):
    """
    Edit booking page template view.
    """
    template_name = 'edit_booking.html'


class DashboardView(TemplateView):
    """
    User's dashboard page template view.
    """
    template_name = 'dashboard.html'


class EditProfileView(TemplateView):
    """
    User's dashboard page template view.
    """
    template_name = 'edit_profile.html'
