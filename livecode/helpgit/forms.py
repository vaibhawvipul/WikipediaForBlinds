from django import forms
from livecode.helpgit.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

	"""
	Handles form for login.
	"""

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    
    """
    Handles form for profile.
    """

    class Meta:
        model=UserProfile
        fields = ('Institution', 'City', 'Country')
