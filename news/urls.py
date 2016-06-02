from django.conf.urls import include, url
from news.views import *

urlpatterns = [
    # url(r'^$', NewsView.as_view(), name='news'),
    url(r'^$', news, name='news'),
    url(r'^(?P<news_id>\d+)$', news_page, name='news_page'),
    url(r'^(?P<news_id>\d+)/comments/add', add_comment, name='add_comment'),
    url(r'^(?P<news_id>\d+)/comments/get', get_comments, name='get_comments')
]
