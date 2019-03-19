#Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

#Models
from comments.models import Comment

class CommentPostView(LoginRequiredMixin,CreateView):
    """Create a new comment to a post"""
    model=Comment
    fields=['description']
    template_name='comments/new.html'

    def form_valid(self, form):
        import pdb; pdb.set_trace()
        return redirect ('feed')

    def form_invalid(self, form):
        import pdb; pdb.set_trace()
        return redirect ('feed')
