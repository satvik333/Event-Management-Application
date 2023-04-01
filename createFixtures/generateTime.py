import datetime
import random

class generatetime:
    def generateRandomTime():
        try:
            start_time = datetime.datetime.strptime("09:00:00", "%H:%M:%S").time()
            end_time = datetime.datetime.strptime("17:00:00", "%H:%M:%S").time()
            start_datetime = datetime.datetime.combine(datetime.datetime.today(), start_time)
            end_datetime = datetime.datetime.combine(datetime.datetime.today(), end_time)
            delta1 = end_datetime - start_datetime
            random_seconds = random.randint(0, int(delta1.total_seconds()))
            random_datetime = start_datetime + datetime.timedelta(seconds=random_seconds)
            return random_datetime.time()
        except Exception as e:
            print('Error while generating time', e)