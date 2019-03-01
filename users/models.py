""""User model of users app"""

#Django
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model of users app.
    Proxy model that extends the base data with other information"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to='users/picture/',
    blank=True,
    null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    posts_count = models.IntegerField(default=0)

    def __str__(self):
        """Return username"""
        return self.user.username
