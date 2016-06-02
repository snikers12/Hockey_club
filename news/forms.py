from django import forms
from models import *
from team.models import Goal, Penalty


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']