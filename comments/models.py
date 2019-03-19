#Django
from django.db import models
from django.contrib.auth.models import User

#Models
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    """Comments model."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    description = models.TextField(max_length=500)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'by @{}'.format(self.user.username)
