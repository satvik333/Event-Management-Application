from generateFixturesDate import fixturedateandtime

class match:
    def generate_match(teams, index, inputFileData):
        try:
            holidayList = inputFileData["holidayList"]
            Event = inputFileData["event"]
            gameType = teams[0]['gameType']
            duration_map = {2: 30, 3: 30}
            duration = duration_map.get(gameType, 180)
            return {
                "date": fixturedateandtime.generateDateAndTime(Event, holidayList),
                "teams": [teams[index]["name"], teams[index + 1]["name"]],
                "duration": duration
            }
        except Exception as e:
            print('Error while generating matches', e)