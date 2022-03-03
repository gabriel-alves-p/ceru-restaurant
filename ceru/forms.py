from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Booking
from django.utils.safestring import mark_safe


class EditProfileForm(UserChangeForm):
    """
    Form to allow users
    to edit their profiles.
    Adds Bootstrap classes "form-control"
    to inputs.
    """
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))  # noqa
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))  # noqa

    class Meta:
        """
        Meta class to set model used in form
        and fields to display in form.
        """
        model = User
        fields = ('username', 'email')


class UpdateBookingForm(forms.ModelForm):
    """
    Form to allow users to edit and
    save their bookings in the database.
    """
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=100, required=True)
    mobile = forms.CharField(max_length=20, required=False)
    date = forms.DateField(required=True)
    time = forms.TimeField(required=True)
    number_of_guests = forms.NumberInput()
    notes = forms.CharField(max_length=245, required=False)

    class Meta:
        """
        Meta class to set model used in form
        and fields to display in form.
        """
        model = Booking
        fields = ('first_name', 'last_name', 'email', 'mobile', 'date', 'time', 'number_of_guests', 'notes')  # noqa


class DeleteUser(forms.Form):
    delete_checkbox = forms.BooleanField(label=mark_safe('Are you sure you want to delete your account?'), required=True)  # noqa

    def __init__(self, *args, **kwargs):
        super(DeleteUser, self).__init__(*args, **kwargs)
