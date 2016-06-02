from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^$', GalleryView.as_view(), name='gallery'),
    url(r'^album_(?P<album_id>\d+)$', album_page, name='album')
]
