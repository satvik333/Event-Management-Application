import datetime
import random
from generateTime import generatetime
from generateScheduledDate import scheduleddate

class fixturedateandtime:
    def generateDateAndTime(Event, holidayist):
        try:
            holidays = [holiday['date'] for holiday in holidayist]
            eventStartDate = datetime.datetime.strptime(Event["startDate"], '%d-%m-%Y').date()
            eventEndDate = datetime.datetime.strptime(Event["endDate"], '%d-%m-%Y').date()
            scheduledDate = scheduleddate.generateScheduledDate(eventStartDate, eventEndDate, holidays)
            random_time = generatetime.generateRandomTime()

            return scheduledDate + ' ' + str(random_time)
        except Exception as e:
            print('Error while generating date', e)