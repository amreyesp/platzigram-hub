#Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from django.shortcuts import redirect

#Models
from comments.models import Comment
from posts.models import Post

class CommentPostView(LoginRequiredMixin,CreateView):
    """Create a new comment to a post"""
    model=Comment
    fields=['description']
    template_name='comments/new.html'
    slug_field = 'id'
    slug_url_kwarg ='post_id'
    queryset= Post.objects.all()

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        form.instance.post = self.get_object()
        form.save()
        return redirect ('feed')


class ListCommentView(LoginRequiredMixin,DetailView):
    model = Comment
    template_name = 'comments/list.html'
    slug_field = 'id'
    slug_url_kwarg ='post_id'
    queryset= Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post=self.get_object()
        context['comments']= Comment.objects.filter(post_id=post.id).order_by('-created')
        context['count']= Comment.objects.filter(post_id=post.id).count()
        return context
