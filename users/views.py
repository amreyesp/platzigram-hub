"""Users views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, FormMixin
from django.urls import reverse_lazy
from django.forms import Form


# Forms
from users.forms import ProfileForm, SignupForm


@login_required
def update_profile(request):
    """Update a user's profile view."""

    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('feed')
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )



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

# def signup_view(request):
#     """Sign up view."""
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect ('login')
#     else:
#         form = SignupForm()
#
#     return render(
#         request=request,
#         template_name='users/signup.html',
#         context={'form':form}
#     )
