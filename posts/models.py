# """Posts models."""

#Django
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Post model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='posts/pictures/')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    likes = models.IntegerField(default=0)

    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)
