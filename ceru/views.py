from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from .models import Booking


class HomeTemplateView(TemplateView):
    """
    Home page template view.
    """
    template_name = 'index.html'
