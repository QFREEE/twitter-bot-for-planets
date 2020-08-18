import csv
import random 
import datetime
import time

SHUFFLED_EXOPLANETS_FILE_NAME = 'shuffledExoplanets.csv'
EXOPLANETS_FILE_NAME = 'exoplanet.csv'
START_DATE = datetime.datetime(2020,8,17,20,00,00,00,tzinfo=datetime.timezone.utc)

def reshuffleCSV():
    with open(EXOPLANETS_FILE_NAME,'r') as r, open(SHUFFLED_EXOPLANETS_FILE_NAME,'w') as w:
        data = r.readlines()
        header, rows = data[0], data[1:]
        random.shuffle(rows)
        rows = '\n'.join([row.strip() for row in rows])
        w.write(header + rows)


def getNameOfPlanet(index):
    NAME_INDEX = 0
    with open(SHUFFLED_EXOPLANETS_FILE_NAME) as csvfile:
        shuffled_exoplants = list(csv.reader(csvfile,delimiter=','))
        return shuffled_exoplants[index][0]

def calculateIndex():
    now = datetime.datetime.now(datetime.timezone.utc)
    
    # getting the time difference from now to startdate 
    elpased_time = now - START_DATE
    elpased_days = elpased_time.days
    return elpased_days + 1

def getDayOfTheWeek():
    week   = ['Sunday', 
              'Monday', 
              'Tuesday', 
              'Wednesday', 
              'Thursday',  
              'Friday', 
              'Saturday']

    now = datetime.datetime.now(datetime.timezone.utc)
    return week[now.isoweekday()]

if __name__ == "__main__":
    getDayOfTheWeek()
    