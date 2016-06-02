from django.db import models
from django.contrib.auth.models import User

from users.models import UserProfile


class News(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='news')
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s : %s" % (self.title, self.publication_date.date())


class Comment(models.Model):
    news = models.ForeignKey('News')
    author = models.ForeignKey(UserProfile)
    comment = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
