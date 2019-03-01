"""Users views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView

# Forms
from users.forms import ProfileForm, SignupForm

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post


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

class DetailUserView(LoginRequiredMixin, DetailView):
    """List detail posts of an user."""
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    template_name = 'users/detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Selecting the posts of an specific user"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context ['posts'] =Post.objects.filter(user=user).order_by('-created')
        return context
