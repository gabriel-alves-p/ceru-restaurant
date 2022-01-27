from django.db import models
from django.contrib.auth.models import User


class Guest(models.Model):
    """
    A class to define the user in the database.
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest')  # noqa
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=80)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"Username: {self.username} | For user: {self.first_name} {self.last_name} | Email: {self.email} | Date of birth: {self.date_of_birth}"  # noqa


class Bookings(models.Model):
    """
    A class to display bookings.
    """
    first_name = models.CharField(max_length=80)
    last_name = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='bookings')  # noqa
    number_of_guests = models.IntegerField(blank=False)
    date = models.DateField()
    time = models.TimeField()
    requirements = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Helper class to order bookings order of inception.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"Booking for {self.number_of_guests}, made by {self.first_name} {self.last_name} on {self.created_on} for the {self.date} at {self.time}"  # noqa
