from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingDisplay.as_view(), name='home')
]
