import os

from django.db import models

from Hockey_club.settings import MEDIA_ROOT


# def get_album_cover_path(instance, filename):
#     return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/media/gallery/' +
#                         instance.album_name, filename)


def get_photo_image_path(instance, filename):
    return os.path.join('gallery', instance.album.album_name, filename)


class Album(models.Model):
    album_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    album_cover = models.ImageField(upload_to='gallery_covers')

    def __unicode__(self):
        return self.album_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            album = Album.objects.get(id=self.id)
            if album.album_name != self.album_name:
                src = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                   'media/gallery/') + album.album_name
                dst = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                   'media/gallery/') + self.album_name
                os.rename(src, dst)
            super(Album, self).save()
        except:
            try:
                Album.objects.get(album_name=self.album_name)
            except:
                os.mkdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                      'media/gallery/') + self.album_name)
                super(Album, self).save()


class Photo(models.Model):
    album = models.ForeignKey('Album', related_name='photos')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=get_photo_image_path)
    date_published = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s : %s" % (self.title, self.date_published.date())
