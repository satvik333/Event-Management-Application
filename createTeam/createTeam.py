import json
from getNumberOfPlayers import numberOfPlayers
from printTeams import createdTeams
from createJsonTeams import jsonTeams
from teamsList import teamList
from extractGameTypeAndPlayers import gameTypeAndPlayers
from readInputFile import readinputfile
from saveTeams import saveteam
from getTeams import getteam
from createJsonFileOfTeams import teamsJsonFile
class createteams:
    def createTeams():
        try:
            inputFilePath = input("Enter file path ")
            inputFileData = readinputfile.read_input_file(inputFilePath)
            gameTypeAndPlayers.extract_game_type_and_players(inputFileData)
            noOfMembers = numberOfPlayers.get_number_of_players()
            playersList = teamList.create_teams_list(noOfMembers)
            teamsJson = jsonTeams.create_teams_json(playersList)
            createdTeams.print_created_teams(teamsJson)
            teamsJsonFile.createJsonFileForTeams(teamsJson)
            saveteam.save_team_to_db(json.loads(teamsJson)['teams'])
            return teamsJson
        except Exception as e:
            print('Error while creating team', e)
   
    createTeams()
    getteam.getTeams(2)


