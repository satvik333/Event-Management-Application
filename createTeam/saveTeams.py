from savePlayers import saveplayers
from databaseConnection import database

cursor = database.connect_to_database()

class saveteam:
    def save_team_to_db(teams):
        try:
            for team in teams:
                cursor.execute("INSERT INTO Team(teamId, name, eventId, gameId) values (?, ?, ?, ?)", team['id'], team['name'], 1, team["gameType"])
                saveplayers.save_players_to_db(team['players'], team['id'])
                cursor.commit()
        except Exception as e:
            print('Error in saving Team', e)