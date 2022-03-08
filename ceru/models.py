from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A class to extend and link
    the User model to the Profile
    model in the database.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} Profile'


class Booking(models.Model):
    """
    A class to make bookings.
    """
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50, null=True)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    notes = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        """
        Helper class to order bookings order of inception.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"Booking for {self.first_name} {self.last_name}, for {self.number_of_guests} guests, for the {self.date} at {self.time}, made on {self.created_on}"  # noqa
