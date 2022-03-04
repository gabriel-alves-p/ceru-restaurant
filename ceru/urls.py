from django.urls import path
from ceru import views


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('edit-booking/<booking_id>', views.update_booking, name='edit-booking'),  # noqa
    path('delete-booking/<booking_id>', views.delete_booking, name='delete-booking'),  # noqa
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('edit-profile/', views.EditProfileView.as_view(), name='edit-profile'),  # noqa
    path('password/', views.EditPasswordView.as_view(template_name='edit_password.html'), name='edit-password'),  # noqa
    path('delete-account/', views.delete_user_view, name='delete-account'),
    path('menus/', views.MenuView.as_view(), name='menus'),
]
