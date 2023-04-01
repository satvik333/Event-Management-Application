import json

class teamsJsonFile:
    def createJsonFileForTeams(teams):
        with open("outputTeams.json", "w", encoding="utf-8") as f:
            json.dump(teams, f, ensure_ascii=False, indent=4)
