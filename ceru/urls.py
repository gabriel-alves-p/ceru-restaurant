from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('accounts/login/dashboard/', views.BookingDisplay.as_view(), name='dashboard'),  # noqa
    path('accounts/signup/dashboard/', views.BookingDisplay.as_view(), name='dashboard'),  # noqa
]
