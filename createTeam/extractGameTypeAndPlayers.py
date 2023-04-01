from Game import Game

class gameTypeAndPlayers:
    def extract_game_type_and_players(inputFileData):
        Game.gameType = inputFileData['gameType']
        Game.players = inputFileData['players']