from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking, Profile


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    A Class to select which admin fields I want
    to apply Summernote to,
    in this case: requirements in Guest model.
    """
    summernote_fields = ('requirements')
    list_filter = ('date', 'time', 'email')
    search_fields = ('email',)
    actions = ['confirm_booking']


admin.site.register(Profile)
