import json

class fixturesJsonFile:
    def createJsonFileForFixtures(fixtures):
        with open("outputFixtures.json", "w", encoding="utf-8") as f:
            json.dump(fixtures, f, ensure_ascii=False, indent=4)