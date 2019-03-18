"""Posts views."""

#Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post


class ListPosts(LoginRequiredMixin, ListView):
    """List existing posts."""
    model = Post
    paginate_by = 4
    template_name = 'posts/feed.html'
    ordering = ('-created',)
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Send the context to filter the following users' on the template
        #through a custom filter
        context ['from_user'] = self.request.user.profile
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create new post view"""

    form_class = PostForm
    template_name = 'posts/new.html'

    def get_object(self, **kwargs):
        """Define queryset. Return user's profile"""
        return self.request.user

    def get_success_url(self,**kwargs):
        """Counting of posts once the success_url is called"""
        user = self.get_object()
        user.profile.posts_count += 1
        user.profile.save()
        return reverse_lazy('feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context for the template"""
        context = super().get_context_data(**kwargs)
        context ['user'] = self.request.user
        context ['profile'] =self.request.user.profile
        return context


def GiveLike(request, post_id):
    """Adding a like to a post"""

    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return redirect('feed')
