from django import forms
from models import *
from team.models import Goal, Penalty

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_scorer_team', 'goal_time', 'goal_scorer', 'assist1', 'assist2']


class PenaltyForm(forms.ModelForm):
    class Meta:
        model = Penalty
        fields = ['team', 'player', 'penalty', 'penalty_minutes', 'penalty_time']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_time', 'text']


class MatchEndForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['ot', 'match_ended']