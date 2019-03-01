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
    paginate_by = 4
    template_name = 'posts/feed.html'
    ordering = ('-created',)
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create new post view"""

    form_class = PostForm
    template_name = 'posts/new.html'
    success_url = reverse_lazy('feed')


    def get_object(self, **kwargs):
        pk = self.request.user
        return pk

    def get_context_data(self, **kwargs):
        """Dynamic counting of posts"""
        user = self.get_object()
        user.profile.posts_count += 1
        user.profile.save()
        """Add user and profile to context for the template"""
        context = super().get_context_data(**kwargs)
        context ['user'] = self.request.user
        context ['profile'] =self.request.user.profile
        return context
