from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^register/$', RegisterFormView.as_view(), name='registration'),
    url(r'^login/', login, name="login"),
    url(r'^logout/', logout, name="logout"),
    url(r'^profile/edit$', UserProfileFormView.as_view(), name='edit_profile')
]
