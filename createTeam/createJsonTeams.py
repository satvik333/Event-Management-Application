from TeamList import TeamList
import json

class jsonTeams:
    def create_teams_json(playersList):
        try:
            teamData = {}
            teamData["teams"] = playersList
            teamData["total"] = TeamList.total
            return json.dumps(teamData)
        except Exception as e:
            print('Error while creating teams json', e)