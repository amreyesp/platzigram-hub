"""Posts views."""

#Django
#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post


# Create your views here.
class ListPosts(LoginRequiredMixin, ListView):
    """List existing posts."""
    model = Post
    paginate_by = 2
    template_name = 'posts/feed.html'
    ordering = ('-created',)
    context_object_name = 'posts'

# @login_required
# def list_posts(request):
#     """List existing posts."""
#     posts = Post.objects.all().order_by('-created')
#     return render(request,'posts/feed.html',{'posts': posts})


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
