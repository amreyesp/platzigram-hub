"""Posts views."""

#Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

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
        #Send the context to filter following users' (through a custom filter)
        #and visualize (or not) the follow button on the template
        context ['from_user'] = self.request.user.profile
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create new post view"""
    model=Post
    fields=['title','photo']
    template_name = 'posts/new.html'

    def form_valid(self, form):
        #Adding the fields that are not in the form
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        form.save()
        #Update the posts_count once the form is validated
        user=self.request.user.profile
        user.posts_count += 1
        user.save()
        return redirect('feed')


def GiveLike(request, post_id):
    """Adding a like to a post"""
    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return redirect('feed')
