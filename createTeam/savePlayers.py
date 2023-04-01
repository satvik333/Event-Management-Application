from databaseConnection import database

cursor = database.connect_to_database()
class saveplayers:
    def save_players_to_db(players, teamId):
        try:
            for player in players:
                cursor.execute("INSERT INTO Player(playerId,playerName) values (?, ?)", player['playerId'], player['name'])
                cursor.execute("INSERT INTO Team_Player(playerId, teamId) values (?, ?)", player['playerId'], teamId)
                cursor.commit()
        except Exception as e:
            print('Error in saving players of Team', e)