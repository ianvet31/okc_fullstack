import json
from django.core.management.base import BaseCommand
import sys
from app.models import Game, Player, Team, Shot
import time
from datetime import date

class Command(BaseCommand):
    help = 'Load data from JSON into the database'

    def handle(self, *args, **options):
        with open('raw_data/games.json', 'r') as f:
            data = json.load(f)
            # Loop through the JSON data and create model instances
            for game_data in data:

                home_team_data = game_data["homeTeam"]
                home_team = Team(
                    id=home_team_data["id"],
                )
                home_team.save()

                away_team_data = game_data["awayTeam"]
                away_team = Team(
                    id=away_team_data["id"],
                )
                away_team.save()

                game = Game(
                    id=game_data["id"],
                    date=str(game_data["date"]),
                    homeTeam_id = home_team_data["id"],
                    awayTeam_id = away_team_data["id"]
                )
                game.save()



                for player_data in home_team_data["players"]:
                    player = Player(
                        id=player_data["id"],
                        isStarter=player_data["isStarter"],
                        minutes = player_data["minutes"],
                        points = player_data["points"],
                        assists = player_data["assists"],
                        offensiveRebounds = player_data["offensiveRebounds"],
                        defensiveRebounds = player_data["defensiveRebounds"],
                        steals = player_data["steals"],
                        blocks = player_data["blocks"],
                        turnovers = player_data["turnovers"],
                        defensiveFouls = player_data["defensiveFouls"],
                        offensiveFouls = player_data["offensiveFouls"],
                        freeThrowsMade = player_data["freeThrowsMade"],
                        freeThrowsAttempted = player_data["freeThrowsAttempted"],
                        twoPointersMade =player_data["twoPointersMade"],
                        twoPointersAttempted = player_data["twoPointersAttempted"],
                        threePointersMade = player_data["threePointersMade"],
                        threePointersAttempted = player_data["threePointersAttempted"]
                    )
                    player.save()
                    home_team.players.add(player)

                    for shot_data in player_data["shots"]:
                        shot = Shot(
                            isMake=shot_data["isMake"],
                            locationX=shot_data["locationX"],
                            locationY=shot_data["locationY"],
                        )
                        shot.save()
                        player.shots.add(shot)

                for player_data in away_team_data["players"]:
                    player = Player(
                        id=player_data["id"],
                        isStarter=player_data["isStarter"],
                        minutes = player_data["minutes"],
                        points = player_data["points"],
                        assists = player_data["assists"],
                        offensiveRebounds = player_data["offensiveRebounds"],
                        defensiveRebounds = player_data["defensiveRebounds"],
                        steals = player_data["steals"],
                        blocks = player_data["blocks"],
                        turnovers = player_data["turnovers"],
                        defensiveFouls = player_data["defensiveFouls"],
                        offensiveFouls = player_data["offensiveFouls"],
                        freeThrowsMade = player_data["freeThrowsMade"],
                        freeThrowsAttempted = player_data["freeThrowsAttempted"],
                        twoPointersMade =player_data["twoPointersMade"],
                        twoPointersAttempted = player_data["twoPointersAttempted"],
                        threePointersMade = player_data["threePointersMade"],
                        threePointersAttempted = player_data["threePointersAttempted"]
                    )
                    player.save()
                    away_team.players.add(player)

                    for shot_data in player_data["shots"]:
                        shot = Shot(
                            isMake=shot_data["isMake"],
                            locationX=shot_data["locationX"],
                            locationY=shot_data["locationY"],
                        )
                        shot.save()
                        player.shots.add(shot)

                game.save()
                
                
                
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))


