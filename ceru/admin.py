from django.contrib import admin
from .models import Guest, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    A Class to select which admin fields I want
    to apply Summernote to,
    in this case: requirements in Guest model.
    """
    summernote_fields = ('requirements')


admin.site.register(Guest)
