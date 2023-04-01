from databaseConnection import database

cursor = database.connect_to_database()
class getteam:
    def getTeams(gameId):
        try:
            cursor.execute("select * from Team, Player, Team_Player where Team.teamId = Team_Player.teamId AND Team_Player.playerId = player.playerId AND gameId = {}".format(gameId))
            result = cursor.fetchall()
            print("Teams are",result)
            return result
        except Exception as e:
            print('Error while retriving data', e)