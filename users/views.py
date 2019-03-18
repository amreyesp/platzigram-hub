"""Users views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse_lazy
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
    """Update view"""

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
        """Selecting the posts of an specific user and pass the context to the
        template"""

        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context ['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context



def follow_user(request, user_to_follow):
    """Adding a user to follow"""

    if request.method == 'POST':
        from_user = request.user.profile
        follow_user = User.objects.get(username=user_to_follow)
        from_user.following.add(follow_user.profile.id)
        #Increment the counter of followers and following
        from_user.following_count += 1
        follow_user.profile.followers_count += 1
        #Save to change data on DB
        from_user.save()
        follow_user.profile.save()

        return redirect('detail_user',username=user_to_follow)


class FollowingDetail(LoginRequiredMixin, DetailView):
    """List detail of users' following"""

    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    template_name = 'users/follow_detail.html'

    def get_context_data(self, **kwargs):
        """Selecting the profiles that user is following and pass the context to the
        template"""
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['profiles'] = user.profile.following.all()
        return context


class FollowerDetail(LoginRequiredMixin, DetailView):
    """List detail of followers"""

    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    template_name = 'users/follow_detail.html'

    def get_context_data(self, **kwargs):
        """Selecting the profiles of the followers"""
        user=self.get_object()
        context=super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.filter(following=user.profile.id)
        return context
