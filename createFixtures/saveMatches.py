from getTeamIds import teamids
import datetime
from databaseConnection import database

cursor = database.connect_to_database()

class savematch:
    def save_match(match, cursor):
        teams = match['teams']
        team_ids = teamids.get_team_ids(teams, cursor)
        date_string = match['date']
        date_object = datetime.datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
        date_string_sql = date_object.strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO Matches(date, firstTeamId, secondTeamId, duration) values (?, ?, ?, ?)", date_string_sql,team_ids[0],team_ids[1],match['duration'] )
        cursor.commit()