from django.shortcuts import render
from django.views.generic import TemplateView

from gallery.models import Album, Photo


class GalleryView(TemplateView):
    template_name = 'gallery/gallery.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        return context


def album_page(request, album_id):
    album = Album.objects.get(id=album_id)
    photos = album.photos.all()

    return render(request, "gallery/album.html", {"photos": photos, "album": album})