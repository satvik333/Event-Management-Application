from databaseConnection import database

cursor = database.connect_to_database()
class teamids:
    def get_team_ids(teams, cursor):
            cursor.execute("SELECT * FROM Team WHERE Team.name IN ('{}')".format("', '".join(teams)))
            rst = cursor.fetchall()
            team_ids = []
            for team in rst:
                team_ids.append(team[0])
            return team_ids