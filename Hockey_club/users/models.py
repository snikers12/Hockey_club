from __future__ import unicode_literals

from django.db import models
from team.models import players_positions
from django.contrib.auth.models import User

gender = {
    ('Male', 'Male'),
    ('Female', 'Female')
}


class UserProfileManager(models.Manager):
    def get_by_natural_key(self):
        return self.get()


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(upload_to='users_avatars', default='users_avatars/default.png')
    gender = models.CharField(max_length=6, choices=gender, default='Male')
    birth_date = models.DateField(default='1970-01-01')
    favorite_position = models.CharField(max_length=2, choices=players_positions, blank=True)
    about = models.TextField(blank=True)

    objects = UserProfileManager()

    def natural_key(self):
        if self.image is not None:
            return (self.user.username, self.image.url)
        else:
            return (self.user.username,)
