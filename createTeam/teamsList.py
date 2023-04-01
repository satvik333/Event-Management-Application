from Game import Game
from TeamList import TeamList

class teamList:
    def create_teams_list(noOfMembers):
        playersList = []
        for i in range(TeamList.total):
            data = {
                "id": i + 1,
                "name": "Team" + str(i),
                "gameType": Game.gameType,
                "players": Game.players[0: noOfMembers]
            }
            playersList.append(data)
            del Game.players[0: noOfMembers]
        TeamList.items = playersList
        return playersList