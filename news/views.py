import json

from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect as redirect
from django.core.urlresolvers import reverse, reverse_lazy

from news.models import *
from news.forms import *
from team.models import Team, Season, TeamSeasonStats


stat_legend = {
    ("GP", "games played"),
    ("P", "points"),
    ("W", "wins"),
    ("L", "loses"),
    ("OT", "overtime loses"),
    ("GF", "goals for"),
    ("GA", "goals against")
}


class NewsView(TemplateView):
    template_name = 'news/news_list.html'

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['images'] = News.objects.all()
        return context


def news_page(request, news_id):
    news_object = News.objects.get(id=news_id)
    comments = news_object.comment_set.all()
    f = CommentForm()
    return render(request, "news/news_page.html", {"news": news_object, "comments": comments, "f": f})


def add_comment(request, news_id):
    response = {}
    f = CommentForm(request.POST)
    if request.is_ajax():
        if request.method == "POST":
            if f.is_valid():
                result_comment = Comment(author=request.user.userprofile, news=News.objects.get(id=news_id))
                result_comment.comment = f.cleaned_data['comment']
                result_comment.save()
                response = serializers.serialize('json', result_comment, use_natural_foreign_keys=True)
    return HttpResponse(response, content_type='application/json')


def get_comments(request, news_id):
    response = {}
    news = News.objects.get(id=news_id)
    comments = news.comment_set.all()
    if request.method == "GET":
        if request.is_ajax():
            response = serializers.serialize('json', comments, use_natural_foreign_keys=True)
    return HttpResponse(response, content_type='application/json')


def news(request):
    news_list = News.objects.all().order_by('-publication_date')
    paginator = Paginator(news_list, 6)
    page = request.GET.get('page')
    try:
        news_post = paginator.page(page)
    except PageNotAnInteger:
        news_post = paginator.page(1)
    except EmptyPage:
        news_post = paginator.page(paginator.num_pages)
    latest_news = news_list[0:6]
    other_news = news_list[6:12]
    legend = stat_legend
    vars = dict(
        news=news_post,
        latest_news=latest_news,
        last_news=latest_news[0],
        other_news=other_news,
        separate_after=other_news[2],
        legend=legend
    )
    return render(request, 'news/news_list_pagination.html', vars)
