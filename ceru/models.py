from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A class to extend and link
    the User model to the Profile
    model in the database.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} Profile'


class Booking(models.Model):
    """
    A class to make bookings.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')  # noqa
    number_of_guests = models.IntegerField(blank=False)
    date = models.DateField()
    time = models.TimeField()
    requirements = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        """
        Helper class to order bookings order of inception.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"Booking for {self.number_of_guests}, made by {self.email} on {self.created_on} for the {self.date} at {self.time}"  # noqa
