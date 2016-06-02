from django.conf.urls import include, url
from django.views.generic import TemplateView
from views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='team/history.html'), name='history'),
    url(r'^stats$', PlayersStatsView.as_view(), name='stats'),
    url(r'^schedule$', ScheduleView.as_view(), name='schedule'),
    # url(r'^standings$', standings, name='standings'),
    url(r'^standings$', StandingsView.as_view(), name='standings'),
    url(r'^roster$', RosterView.as_view(), name='roster'),
    # url(r'^/team/schedule/(?P<match_id>)$', match_info, name='match_info'),
    # url(r'^test$', test, name='test')
    url(r'^online/(?P<online_id>\d+)$', online, name='online'),
    url(r'^online/(?P<online_id>\d+)/get_events$', get_events, name='get_events'),
    url(r'^online/(?P<online_id>\d+)/get_score$', get_score, name='get_score'),
    url(r'^online/get_team(?P<online_id>\d+)$', get_teams, name='get_teams'),
    url(r'^online/get_players(?P<team_id>\d+)$', get_players, name='get_players')
]
