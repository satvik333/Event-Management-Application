from getTeamIds import teamids
from saveMatches import savematch
from databaseConnection import database

cursor = database.connect_to_database()

class savefixture:
    def save_fixtures(matches, cursor):
        try:
            for match in matches:
                savematch.save_match(match, cursor)
        except Exception as e:
            print('Error while saving fixtures', e)