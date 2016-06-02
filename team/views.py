import json

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core import serializers
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView

from team.forms import EventForm, GoalForm, PenaltyForm, MatchEndForm
from team.models import *


def standings(request):
    stats = TeamSeasonStats.objects.all()
    return render(request, "team/standings.html", {"stats": stats})


class StandingsView(TemplateView):
    template_name = 'team/standings.html'

    def get_context_data(self, **kwargs):
        context = super(StandingsView, self).get_context_data(**kwargs)

        context["stats"] = TeamSeasonStats.objects.filter(season=Season.objects.last()).order_by(
            '-points', 'games_played', '-wins', 'loses',
            '-goals_for', 'goals_against')
        return context


class RosterView(TemplateView):
    template_name = 'team/roster.html'

    def get_context_data(self, **kwargs):
        context = super(RosterView, self).get_context_data(**kwargs)

        context["stuff"] = TeamStuff.objects.filter(team=Team.objects.get(id=3)).order_by('position')
        context["players"] = Player.objects.filter(team=Team.objects.get(id=3)).order_by('number')
        return context


class PlayersStatsView(TemplateView):
    template_name = 'team/stats.html'

    def get_context_data(self, **kwargs):
        context = super(PlayersStatsView, self).get_context_data(**kwargs)

        context["goaltenders"] = GoaltenderStats.objects.filter(season=Season.objects.last()).order_by(
            '-wins', 'goals_against', '-games_played')
        context["defencemans"] = FieldPlayerStats.objects.filter(season=Season.objects.last(),
                                                                 player__position=("D")).order_by('-points', '-goals',
                                                                                                  '-assists',
                                                                                                  'games_played')
        context["forwards"] = FieldPlayerStats.objects.filter(player__position__in=["RW", "LW", "C"],
                                                              season=Season.objects.last()).order_by('-points',
                                                                                                     '-goals',
                                                                                                     '-assists',
                                                                                                     'games_played')
        return context


class ScheduleView(TemplateView):
    template_name = 'team/schedule.html'

    def get_context_data(self, **kwargs):
        context = super(ScheduleView, self).get_context_data(**kwargs)
        context["matchs"] = Match.objects.filter(season=Season.objects.last()).order_by('-date')
        return context


def get_events(request, online_id):
    response = {}
    online = Online.objects.get(id=online_id)
    events = online.events.all()
    if request.method == "GET":
        if request.is_ajax():
            response = serializers.serialize('json', events)
    return HttpResponse(response, content_type='application/json')


def get_score(request, online_id):
    response = {}
    match = Online.objects.get(id=online_id).match
    if request.method == "GET":
        if request.is_ajax():
            response['home_score'] = match.home_score
            response['guest_score'] = match.guest_score
    return HttpResponse(json.dumps(response), content_type='application/json')


def online(request, online_id):
    online = Online.objects.get(id=online_id)
    events = online.events.all().order_by('event_time')

    if request.method == "GET":
        goal_form = GoalForm()
        penalty_form = PenaltyForm()
        event_form = EventForm()
        match_end_form = MatchEndForm()
        return render(request, "team/online_form.html",
                      {"events": events, "goal_form": goal_form, "penalty_form": penalty_form,
                       "event_form": event_form, "match_end_form": match_end_form, "online": online})
    elif request.method == "POST":
        goal_form = GoalForm(request.POST)
        penalty_form = PenaltyForm(request.POST)
        event_form = EventForm(request.POST)
        match_end_form = MatchEndForm(request.POST)
        if goal_form.is_valid():
            event = Goal(match=Online.objects.get(id=online_id).match)
            event.goal_scorer_team = goal_form.cleaned_data['goal_scorer_team']
            event.goal_time = goal_form.cleaned_data['goal_time']
            event.goal_scorer = goal_form.cleaned_data['goal_scorer']
            event.assist1 = goal_form.cleaned_data['assist1']
            event.assist2 = goal_form.cleaned_data['assist2']
            event.save()
            return redirect(reverse("team:online", args=(online_id,)))
        elif penalty_form.is_valid():
            penalty = Penalty(match=Online.objects.get(id=online_id).match)
            penalty.team = penalty_form.cleaned_data['team']
            penalty.player = penalty_form.cleaned_data['player']
            penalty.penalty = penalty_form.cleaned_data['penalty']
            penalty.penalty_minutes = penalty_form.cleaned_data['penalty_minutes']
            penalty.penalty_time = penalty_form.cleaned_data['penalty_time']
            penalty.save()
            return redirect(reverse("team:online", args=(online_id,)))
        elif event_form.is_valid():
            event = Event(online=Online.objects.get(id=online_id))
            event.event_time = event_form.cleaned_data['event_time']
            event.text = event_form.cleaned_data['text']
            event.save()
            return redirect(reverse("team:online", args=(online_id,)))
        elif match_end_form.is_valid():
            match = Online.objects.get(id=online_id).match
            match.match_ended = match_end_form.cleaned_data['match_ended']
            match.ot = match_end_form.cleaned_data['ot']
            match.save()
            return redirect(reverse("team:online", args=(online_id,)))
        else:
            return render(request, "team/online_form.html",
                          {"events": events, "goal_form": goal_form, "penalty_form": penalty_form,
                           "event_form": event_form, "match_end_form": match_end_form, "online": online})
    else:
        return HttpResponse("405")


def get_teams(request, online_id):
    match = Online.objects.get(id=online_id).match
    teams = [match.home, match.guest]
    response = serializers.serialize('json', teams)
    return HttpResponse(response, content_type='application/json')


def get_players(request, team_id):
    players = Player.objects.filter(team=Team.objects.get(id=team_id))
    response = serializers.serialize('json', players)
    return HttpResponse(response, content_type='application/json')
