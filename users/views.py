"""Users views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse, reverse_lazy

# Forms
from users.forms import ProfileForm, SignupForm

# Models
from django.contrib.auth.models import User
from users.models import Profile


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logut view."""

    template_name = 'users/logged_out.html'

class SignupView(FormView):
    """Signup view"""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return redirect ('login')

class UpdateProfileView (LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'users/update_profile.html'
    success_url = reverse_lazy('feed')

    def get_object(self):
        return self.request.user.profile
