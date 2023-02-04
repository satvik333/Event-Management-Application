import json
from Event import Event
from FixtureList import FixtureList
from Ocassion import Occasion
import datetime
import random
import datetime
import pyodbc
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=ITT-SATVIK-MS;DATABASE=ISCdatabase;Trusted_Connection=yes;')
cursor = connection.cursor()

def saveFixtures(matches):
    for match in matches:
        teams = match['teams']
        for team in teams:
            print(team,'ttttttttttt')
            cursor.execute("select * from Team where Team.name = {}".format(team))
            rst = cursor.fetchall()
            print(rst,'/////////////////')
        # cursor.execute("INSERT INTO Matches(date, firstTeamId, secondTeamId, duration) values (?, ?, ?, ?)", match['date'], )

def generateDate(Event, holidayist):
    holidays = []
    for i in holidayist:
        holidays.append(i['date'])
    eventStartDate = datetime.datetime.strptime(Event["startDate"], '%d-%m-%Y').date()
    eventEndDate = datetime.datetime.strptime(Event["endDate"], '%d-%m-%Y').date()
    start_date = datetime.date(int(eventStartDate.strftime('%Y')), int(eventStartDate.strftime('%m')), int(eventStartDate.strftime('%d')))
    end_date = datetime.date(int(eventEndDate.strftime('%Y')), int(eventEndDate.strftime('%m')), int(eventEndDate.strftime('%d')))
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + datetime.timedelta(days=random_days)
    scheduledDate = random_date.strftime('%d-%m-%Y')
    maxDate = random_date.strftime('%Y-%m-%d')

    while scheduledDate <= maxDate:
        if scheduledDate not in holidays:
            return scheduledDate
        scheduledDate += scheduledDate(days=1)

    start_time = datetime.datetime.strptime("09:00:00", "%H:%M:%S").time()
    end_time = datetime.datetime.strptime("17:00:00", "%H:%M:%S").time()
    start_datetime = datetime.datetime.combine(datetime.datetime.today(), start_time)
    end_datetime = datetime.datetime.combine(datetime.datetime.today(), end_time)
    delta1 = end_datetime - start_datetime
    random_seconds = random.randint(0, int(delta1.total_seconds()))
    random_datetime = start_datetime + datetime.timedelta(seconds=random_seconds)
    random_time = random_datetime.time()

    return scheduledDate + ' ' + str(random_time)

def readJsonFile(filePath):
    try:
        file = open(filePath)
        fileData = json.loads(file.read())
        return fileData
    except:
        print('Error while reading a file')

def createFixtures(teamList, holidayList, Event):
    teams = teamList["teams"]
    gameType = ''
    matches = []
    for i in range(0, len(teams), 2):
        gameType = teams[i]['gameType']
        duration = 0
        if (gameType == 2 or gameType == 3):
            duration = 30
        else:
            duration = 180
        match = {
            "date": generateDate(Event, holidayList),
            "teams": [teams[i]["name"], teams[i + 1]["name"]],
            "duration": duration
        }
        matches.append(match)
    output_data = {
        "gameId": gameType,
        "matches": matches,
    }
    FixtureList.matches = output_data["matches"]
    # saveFixtures(FixtureList.matches)
    print(output_data)
    return output_data


inputFileData = readJsonFile('C:/Users/satvik.ms/Desktop/L-C-Final-Project/FixtureInput.json')

teamList = inputFileData["listOfTeams"]
holidayList = inputFileData["holidayList"]
Event = inputFileData["event"]
createFixtures(teamList, holidayList, Event)