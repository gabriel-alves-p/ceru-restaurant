from django.db import models
from django.contrib.auth.models import User


# class Guest(models.Model):
#     """
#     A class to define the user in the database.
#     """
#     email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest')  # noqa
#     password = models.CharField(max_length=80)
#     first_name = models.CharField(max_length=80)
#     last_name = models.CharField(max_length=80)
#     date_of_birth = models.DateField()

#     def __str__(self):
#         return f"Guest: {self.first_name} {self.last_name} | Email: {self.email}"  # noqa

class Booking(models.Model):
    """
    A class to make bookings.
    """
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking', null=True)  # noqa
    number_of_guests = models.IntegerField(blank=False)
    date = models.DateField()
    time = models.TimeField()
    requirements = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        """
        Helper class to order bookings order of inception.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"Booking for {self.number_of_guests}, made by {self.first_name} {self.last_name} {self.email} on {self.created_on} for the {self.date} at {self.time}"  # noqa
