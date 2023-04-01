from TeamList import TeamList
from Game import Game

class checkforgametype:
    def checkForGameTypeAndGetNoOfPlayers():
        options = {
            1: 11,
            2: 2
        }
        noOfMembers = options.get(Game.gameType, 1)
        try:
            TeamList.total = int(len(Game.players) / noOfMembers)
            if len(Game.players) < noOfMembers or len(Game.players) % noOfMembers != 0:
                raise ValueError('Cannot create teams')
        except ValueError as e:
            print(e)
        return noOfMembers