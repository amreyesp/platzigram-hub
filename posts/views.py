"""Posts views."""

#Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import DetailView

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post
from django.contrib.auth.models import User


class ListPosts(LoginRequiredMixin, ListView):
    """List existing posts."""
    model = Post
    paginate_by = 2
    template_name = 'posts/feed.html'
    ordering = ('-created',)
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create new post view"""

    form_class = PostForm
    template_name = 'posts/new.html'
    success_url = reverse_lazy('feed')

    def get_context_data(self, **kwargs):
        """Add user profile and context"""
        context = super().get_context_data(**kwargs)
        context ['user'] = self.request.user
        context ['profile'] =self.request.user.profile
        return context

class DetailPostView(LoginRequiredMixin, DetailView):
    """List detail posts of an user."""
    model = Post
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        """Selecting the posts of an specific user"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context ['posts'] =Post.objects.filter(user=user).order_by('-created')
        return context
