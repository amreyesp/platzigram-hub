"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirm = forms.CharField(max_length=70, widget=forms.PasswordInput())
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=4, max_length=50)
    email = forms.CharField(min_length=8, max_length=70, widget=forms.EmailInput())

    def clean_username(self):
        """User name must be unique"""
        username  =self.cleaned_data['username']
        username_taken= User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Password confirmation validation"""
        data = super().clean()

        password = data ['password']
        password_confirm = data ['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError('Password does not match.')
        return data

    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirm')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.ModelForm):
    """Profile form."""

    class Meta:
        model = Profile
        fields = ('website', 'biography', 'phone_number', 'picture')
