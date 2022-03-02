from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms


class EditProfileForm(UserChangeForm):
    """
    Form to allow users
    to edit their profiles.
    Adds Bootstrap classes "form-control"
    to inputs.
    """
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))  # noqa
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))  # noqa

    class Meta:
        """
        Meta class to set model used in form
        and fields to display in form.
        """
        model = User
        fields = ('username', 'email')
