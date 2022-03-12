from django.shortcuts import render, redirect
from django.views import generic
from django.core.mail import send_mail
from django.views.generic.base import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Booking
from .forms import EditProfileForm, UpdateBookingForm, DeleteUser


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
        messages.success(request, 'Booking made successfully.')
        return redirect('dashboard')


class MenuView(TemplateView):
    """
    Edit booking page template view.
    """
    template_name = 'menus.html'


class DashboardView(generic.ListView):
    """
    User's dashboard page template view.
    """
    template_name = 'dashboard.html'
    model = Booking
    paginate_by = 3

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


class EditProfileView(generic.UpdateView):
    """
    Class renders the view for edit_profile.html
    and gets user to autofill user's details on
    form inputs.
    """
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('edit-profile')

    def get_object(self):
        """
        Returns current user to template.
        """
        return self.request.user


class EditPasswordView(PasswordChangeView):
    """
    View to allow users to update their passwords.
    """
    form_class = PasswordChangeForm
    success_url = reverse_lazy('edit-profile')


# --------------------------------------------------- FUNCTION-BASED VIEWS
def home_template_view(request):
    """
    Function
    """
    if request.method == "POST":
        message_first_name = request.POST['firstName']
        message_last_name = request.POST['lastName']
        message_email = request.POST['emailAddress']
        message_mobile = request.POST['phoneNumber']
        message = request.POST['query']

        send_mail(
            message_first_name + message_last_name,  # subject
            message_mobile + message,  # message
            message_email,  # from
            ['cerudiner@gmail.com'],  # to mail
        )
        messages.info(request, "Your message has been sent.")
        return render(request, 'index.html', {'message_first_name': message_first_name})  # noqa
    else:
        return render(request, 'index.html', {})


def delete_user_view(request):
    """
    Function based view used to delete
    a user's account if they wish to do
    so themselves.
    """
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DeleteUser(request.POST)

            if form.is_valid():
                if request.POST["delete_checkbox"]:
                    rem = User.objects.get(username=request.user)
                    if rem is not None:
                        rem.delete()
                        logout(request)
                        messages.info(request, "Your account has been deleted.")  # noqa
                        return redirect("home")
                    else:
                        messages.info(request, "There was an error.")
        else:
            form = DeleteUser()
        context = {'form': form}
        return render(request, 'delete_account.html', context)
    if request.user.is_anonymous:
        return HttpResponse(render(request, "401.html"), status=401)


def update_booking(request, booking_id):
    """
    Function based view to allow user
    to update a booking that has been made.
    """
    booking = Booking.objects.get(pk=booking_id)
    form = UpdateBookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        form.save()
        messages.success(request, 'Booking updated successfully.')
        return redirect('dashboard')
    return render(request, 'edit_booking.html', {'booking': booking, 'form': form})  # noqa


def delete_booking(request, booking_id):
    """
    Function based view to allow user
    to delete a booking that has been made.
    """
    booking = Booking.objects.get(pk=booking_id)
    booking.delete()
    messages.success(request, 'Booking deleted successfully.')
    return redirect('dashboard')
