from django.contrib import admin
from django import forms

from models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Team._meta.fields if field.name != "id"]


class TeamSeasonStatsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TeamSeasonStats._meta.fields if field.name != "id"]


class PlayerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Player._meta.fields if field.name != "id"]


class TeamStuffAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TeamStuff._meta.fields if field.name != "id"]


class FieldPlayerStatsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FieldPlayerStats._meta.fields if field.name != "id"]


class GoaltenderStatsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GoaltenderStats._meta.fields if field.name != "id"]


class GoalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Goal._meta.fields if field.name != "id"]


class ArenaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Arena._meta.fields if field.name != "id"]


# class MatchForm(forms.ModelForm):
#     class Meta:
#         model = Match
#         fields = [field.name for field in Match._meta.fields if field.name != "id"]
#         widgets = {
#             'time': forms.TimeInput(format="%M:%S"),
#         }


class MatchAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Match._meta.fields if field.name != "id"]


class MatchStatsAdmin(admin.ModelAdmin):
    list_filter = ['home_players', 'guest_players']
    filter_horizontal = ['home_players', 'guest_players']


admin.site.register(Team, TeamAdmin)
admin.site.register(TeamSeasonStats, TeamSeasonStatsAdmin)
admin.site.register(Season)
admin.site.register(Player, PlayerAdmin)
admin.site.register(TeamStuff, TeamStuffAdmin)
admin.site.register(FieldPlayerStats, FieldPlayerStatsAdmin)
admin.site.register(GoaltenderStats, GoaltenderStatsAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Arena, ArenaAdmin)
admin.site.register(Penalty)
admin.site.register(Online)
admin.site.register(Event)
# admin.site.register(MatchStats, MatchStatsAdmin)