from django.db import models
from django.utils.datetime_safe import datetime

players_positions = {
    ("D", "Defenceman"),
    ("LW", "Left Winger"),
    ("RW", "Right Winger"),
    ("C", "Center"),
    ("G", "Goaltender")
}

stuff_positions = {
    ("Head coach", "HC"),
    ("Coach", "C"),
    ("Goaltender's coach", "GC"),
    ("President", "P"),
    ("General manager", "GM"),
    ("Masseur", "M"),
    ("Doctor", "D")
}

match_end = {
    ("OT", "Overtime"),
    ("SO", "Shootout")
}

penalty = {
    ("Tripping", "TR"),
    ("Hooking", "HK"),
    ("Interference", "INT"),
    ("Too many man on ice", "TMM"),
    ("High stick", "HS"),
    ("Kneeing", "KN")
}


class Team(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    founded = models.DateField()
    arena = models.ForeignKey('Arena')
    is_alive = models.BooleanField()
    logo = models.ImageField(upload_to='teams_logos')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.is_alive:
            try:
                team = Team.objects.get(id=self.id)
            except:
                super(Team, self).save()
                new_team_stats = TeamSeasonStats(team=self, season=Season.objects.order_by("-years").last())
                new_team_stats.save()
        super(Team, self).save()

    def __unicode__(self):
        return self.name


class Arena(models.Model):
    name = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveSmallIntegerField()
    founded = models.DateField()

    def __unicode__(self):
        return self.name


class Season(models.Model):
    years = models.CharField(max_length=9)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Season, self).save()
        for team in Team.objects.all():
            if team.is_alive:
                new_team_stats = TeamSeasonStats(season=self, team=team)
                new_team_stats.save()
        for player in Player.objects.all():
            if player.playing_now:
                if player.position == "G":
                    new_player_stats = GoaltenderStats(season=self, player=player, team=player.team)
                    new_player_stats.save()
                else:
                    new_player_stats = FieldPlayerStats(season=self, player=player, team=player.team)
                    new_player_stats.save()

    def __unicode__(self):
        return self.years


class TeamSeasonStats(models.Model):
    class Meta:
        unique_together = ['team', 'season']

    team = models.ForeignKey('Team')
    season = models.ForeignKey('Season')
    games_played = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    ot = models.PositiveSmallIntegerField(default=0)
    loses = models.PositiveSmallIntegerField(default=0)
    goals_for = models.PositiveSmallIntegerField(default=0)
    goals_against = models.PositiveSmallIntegerField(default=0)
    points = models.PositiveSmallIntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.games_played = self.wins + self.ot + self.loses
        self.points = self.wins * 2 + self.ot

        super(TeamSeasonStats, self).save()

    def __unicode__(self):
        return "%s %s" % (self.team.name, self.season.years)


class TeamStuff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.ForeignKey('Team', default=1)
    position = models.CharField(max_length=50, choices=stuff_positions)

    def __unicode__(self):
        return "%s %s: %s" % (self.first_name, self.last_name, self.position)


class Player(models.Model):
    class Meta:
        unique_together = ['number', 'team']

    number = models.PositiveSmallIntegerField()
    team = models.ForeignKey('Team', default=1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=players_positions)
    birthday = models.DateField()
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    playing_now = models.BooleanField(default=True)

    def __unicode__(self):
        return "#%s | %s %s: %s" % (self.number, self.first_name, self.last_name, self.position)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Player, self).save()
        if self.playing_now:
            if self.position == "G":
                new_player_stats = GoaltenderStats(season=Season.objects.order_by("-years").last(), player=self,
                                                   team=self.team)
                new_player_stats.save()
            else:
                new_player_stats = FieldPlayerStats(season=Season.objects.order_by("-years").last(), player=self,
                                                    team=self.team)
                new_player_stats.save()


class FieldPlayerStats(models.Model):
    class Meta:
        unique_together = ['player', 'season', 'team']

    player = models.ForeignKey('Player')
    season = models.ForeignKey('Season')
    team = models.ForeignKey('Team')
    games_played = models.PositiveSmallIntegerField(default=0)
    goals = models.PositiveSmallIntegerField(default=0)
    assists = models.PositiveSmallIntegerField(default=0)
    points = models.PositiveSmallIntegerField(default=0)
    penalty_minutes = models.PositiveSmallIntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.points = self.goals + self.assists
        super(FieldPlayerStats, self).save()

    def __unicode__(self):
        return "#%s | %s season %s" % (self.player.number, self.player.last_name, self.season.years)


class GoaltenderStats(models.Model):
    class Meta:
        unique_together = ['player', 'season', 'team']

    player = models.ForeignKey('Player')
    season = models.ForeignKey('Season')
    team = models.ForeignKey('Team')
    games_played = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    goals_against = models.PositiveSmallIntegerField(default=0)
    null = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return "#%s | %s season %s" % (self.player.number, self.player.last_name, self.season.years)


class Match(models.Model):
    class Meta:
        unique_together = (('date', 'home'), ('date', 'guest'))

    date = models.DateField(default=datetime.now())
    season = models.ForeignKey('Season', default=0)
    home = models.ForeignKey('Team', related_name="home")
    guest = models.ForeignKey('Team', related_name="guest")
    home_score = models.PositiveSmallIntegerField(default=0)
    guest_score = models.PositiveSmallIntegerField(default=0)
    home_players = models.ManyToManyField('Player', related_name='home_players')
    guest_players = models.ManyToManyField('Player', related_name='guest_players')
    ot = models.CharField(max_length=2, choices=match_end, blank=True)
    match_ended = models.BooleanField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            match = Match.objects.get(id=self.id)
            if not match.match_ended and self.match_ended:
                Match.points_count(self)
                Match.game_played_inc(self)
            super(Match, self).save()
        except:
            if self.match_ended:
                Match.points_count(self)
                Match.game_played_inc(self)
            super(Match, self).save()
            online = Online(match=self)
            online.save()

    def game_played_inc(self):
        home_players = self.home_players.all()
        guest_players = self.guest_players.all()
        for home_player in home_players:
            if home_player.position == 'G':
                goaltenter_stats = GoaltenderStats.objects.get(season=self.season, player=home_player)
                goaltenter_stats.games_played += 1
                goaltenter_stats.save()
            else:
                field_player_stats = FieldPlayerStats.objects.get(season=self.season, player=home_player)
                field_player_stats.games_played += 1
                field_player_stats.save()
        for guest_player in guest_players:
            if guest_player.position == 'G':
                goaltenter_stats = GoaltenderStats.objects.get(season=self.season, player=guest_player)
                goaltenter_stats.games_played += 1
                goaltenter_stats.save()
            else:
                field_player_stats = FieldPlayerStats.objects.get(season=self.season, player=guest_player)
                field_player_stats.games_played += 1
                field_player_stats.save()

    def points_count(self):
        home_team = TeamSeasonStats.objects.get(team=self.home, season=self.season)
        guest_team = TeamSeasonStats.objects.get(team=self.guest, season=self.season)

        home_team.games_played += 1
        home_team.goals_for += self.home_score
        home_team.goals_against += self.guest_score

        guest_team.games_played += 1
        guest_team.goals_for += self.guest_score
        guest_team.goals_against += self.home_score

        if self.home_score > self.guest_score:
            if self.ot == "OT" or self.ot == "SO":
                guest_team.ot += 1
            else:
                guest_team.loses += 1
            home_team.wins += 1
        else:
            if self.ot == "OT" or self.ot == "SO":
                home_team.ot += 1
            else:
                home_team.loses += 1
            guest_team.wins += 1
        home_team.save()
        guest_team.save()

    def __unicode__(self):
        return "%s | %s %s:%s %s" % (self.date, self.home.name, self.home_score, self.guest_score, self.guest.name)


class Goal(models.Model):
    match = models.ForeignKey('Match')
    goal_scorer_team = models.ForeignKey('Team')
    goal_time = models.TimeField(default="00:00")
    goal_scorer = models.ForeignKey('Player', related_name='goal_scorer')
    assist1 = models.ForeignKey('Player', related_name='assist1', blank=True, null=True)
    assist2 = models.ForeignKey('Player', related_name='assist2', blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            Goal.objects.get(id=self.id)
            super(Goal, self).save()
        except:
            if not self.match.match_ended:
                if self.goal_scorer != self.assist1 and self.goal_scorer != self.assist2 and self.assist1 != self.assist2:

                    message = self.goal_scorer_team.name + " scores! Goal scored by " + self.goal_scorer.__unicode__() + ". "
                    match = Match.objects.get(id=self.match_id)
                    if self.goal_scorer_team == self.match.home:
                        match.home_score += 1
                    elif self.goal_scorer_team == self.match.guest:
                        match.guest_score += 1
                    match.save()

                    if self.assist1 and self.assist2:
                        message += "Assists made by " + self.assist1.__unicode__() + " and " + self.assist2.__unicode__() + "."
                        goal_scorer_stats = FieldPlayerStats.objects.get(player=self.goal_scorer,
                                                                         season=self.match.season)
                        goal_scorer_stats.goals += 1
                        goal_scorer_stats.save()

                        assist1_stats = FieldPlayerStats.objects.get(player=self.assist1, season=self.match.season)
                        assist1_stats.assists += 1
                        assist1_stats.save()

                        assist2_stats = FieldPlayerStats.objects.get(player=self.assist2, season=self.match.season)
                        assist2_stats.assists += 1
                        assist2_stats.save()
                    elif not self.assist1 and not self.assist2:
                        message += "Without assists."
                        goal_scorer_stats = FieldPlayerStats.objects.get(player=self.goal_scorer, season=self.match.season)
                        goal_scorer_stats.goals += 1
                        goal_scorer_stats.save()
                    elif not self.assist2:
                        if self.goal_scorer != self.assist1:
                            message += "Assist made by " + self.assist1.__unicode__() + "."
                            goal_scorer_stats = FieldPlayerStats.objects.get(player=self.goal_scorer,
                                                                             season=self.match.season)
                            goal_scorer_stats.goals += 1
                            goal_scorer_stats.save()

                            assist1_stats = FieldPlayerStats.objects.get(player=self.assist1, season=self.match.season)
                            assist1_stats.assists += 1
                            assist1_stats.save()
                    event = Event(online=Online.objects.get(match=self.match), event_time=self.goal_time, text=message)
                    event.save()
                    super(Goal, self).save()

    def __unicode__(self):
        return "%s. Goal:%s Assists:%s %s" % (self.match, self.goal_scorer, self.assist1, self.assist2)


class Penalty(models.Model):
    match = models.ForeignKey("Match", related_name="match")
    team = models.ForeignKey("Team", related_name="team")
    player = models.ForeignKey("Player", related_name="player")
    penalty = models.CharField(max_length=50, choices=penalty)
    penalty_minutes = models.PositiveSmallIntegerField()
    penalty_time = models.TimeField(default="00:00")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        message = "Penalty for " + self.team.name + " team. " + self.player.__unicode__() + " deleted for " + \
                  self.penalty + " for " + str(self.penalty_minutes) + " minutes."
        event = Event(online=Online.objects.get(match=self.match), event_time=self.penalty_time, text=message)
        event.save()
        player_stats = FieldPlayerStats.objects.get(player=self.player)
        player_stats.penalty_minutes += self.penalty_minutes
        player_stats.save()
        super(Penalty, self).save()


class Online(models.Model):
    match = models.OneToOneField('Match')


class Event(models.Model):
    online = models.ForeignKey('Online', related_name='events')
    event_time = models.TimeField(default="00:00")
    text = models.TextField()
