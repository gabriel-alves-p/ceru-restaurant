from django.urls import path
from ceru import views


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('edit-booking/', views.EditBookingView.as_view(), name='edit-booking'),  # noqa
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('edit-profile/', views.EditProfileView.as_view(), name='edit-profile'),  # noqa
]
