# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Contains models related to stats"""
from django.db import models


class Shot(models.Model):
    isMake = models.BooleanField()
    locationX = models.FloatField()
    locationY = models.FloatField()

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    isStarter = models.BooleanField()
    minutes = models.IntegerField()
    points = models.IntegerField()
    assists = models.IntegerField()
    offensiveRebounds = models.IntegerField()
    defensiveRebounds = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnovers = models.IntegerField()
    defensiveFouls = models.IntegerField()
    offensiveFouls = models.IntegerField()
    freeThrowsMade = models.IntegerField()
    freeThrowsAttempted = models.IntegerField()
    twoPointersMade = models.IntegerField()
    twoPointersAttempted = models.IntegerField()
    threePointersMade = models.IntegerField()
    threePointersAttempted = models.IntegerField()
    shots = models.ManyToManyField(Shot)

class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    players = models.ManyToManyField(Player)

class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(default="0100-00-01")
    homeTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home")
    awayTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away")
