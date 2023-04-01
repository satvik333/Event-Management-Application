import json
from Event import Event
from generateMatches import match
from FixtureList import FixtureList
from readJsonFile import readjson
from saveFixtures import savefixture
from databaseConnection import database
from printFixtures import createdFixtures
from createJsonFileOfFixtures import fixturesJsonFile

cursor = database.connect_to_database()
class createfixtures:
    def create_fixtures():
        try:
            inputFilePath = input("Enter the input file path ")
            inputFileData = readjson.readJsonFile(inputFilePath)
            teamList = inputFileData["listOfTeams"]
            teams = teamList["teams"]
            if (len(teams) % 2 != 0):
                return "Cannot create fixtures with odd number of teams"

            gameType = teams[0]['gameType']
            matches = [match.generate_match(teams, index, inputFileData) for index in range(0, len(teams), 2)]

            FixtureList.matches = matches

            fixtures = {
                "gameId": gameType,
                "matches": matches,
            }
            createdFixtures.print_created_fixtures(fixtures)
            fixturesJsonFile.createJsonFileForFixtures(fixtures)
            savefixture.save_fixtures(FixtureList.matches, cursor)
            return json.dumps(fixtures)
        except Exception as e:
            print('Error while creating fixture', e)

createfixtures.create_fixtures()