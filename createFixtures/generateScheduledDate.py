from checkForHolidays import holidayslist
import datetime
import random

class scheduleddate:
    def generateScheduledDate(eventStartDate, eventEndDate, holidays):
        try:
            delta = eventEndDate - eventStartDate
            random_days = random.randint(0, delta.days)
            random_date = eventStartDate + datetime.timedelta(days=random_days)
            scheduledDate = random_date.strftime('%d-%m-%Y')
            maxDate = random_date.strftime('%Y-%m-%d')

            while holidayslist.isScheduledDateInHolidays(scheduledDate, holidays):
                scheduledDate = (datetime.datetime.strptime(scheduledDate, '%d-%m-%Y') + datetime.timedelta(days=1)).strftime('%d-%m-%Y')
            return scheduledDate
        except Exception as e:
            print('Error while generating scheduled date', e)