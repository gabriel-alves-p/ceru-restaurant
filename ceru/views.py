from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.contrib import messages
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

    def post(self, request):
        """
        Handles post requests.
        """
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        date = request.POST.get("date")
        time = request.POST.get("time")
        quantity = request.POST.get("quantity")
        notes = request.POST.get("notes")
        user = request.user

        booking = Booking.objects.create(
            user=user,
            first_name=fname,
            last_name=lname,
            email=email,
            mobile=mobile,
            date=date,
            time=time,
            number_of_guests=quantity,
            notes=notes
        )

        booking.save()

        messages.add_message(request, messages.SUCCESS, "Your booking has been acccepted.")  # noqa
        return render(request, 'booking_form.html')


class EditBookingView(TemplateView):
    """
    Edit booking page template view.
    """
    template_name = 'edit_booking.html'


class DashboardView(ListView):
    """
    User's dashboard page template view.
    """
    template_name = 'dashboard.html'
    model = Booking

    def get_queryset(self, *args, **kwargs):
        """
        Filters bookings and displays user's bookings
        to user, and all bookings to admin.
        """
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class EditProfileView(TemplateView):
    """
    User's dashboard page template view.
    """
    template_name = 'edit_profile.html'
