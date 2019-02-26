"""Posts views."""

#Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post


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
