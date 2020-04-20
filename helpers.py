import datetime
import string, random

def getTimestampSeconds():
    return int(datetime.datetime.timestamp(datetime.datetime.now()))

def getDateHuman():
    return datetime.datetime.fromtimestamp(getTimestampSeconds()).isoformat()

def generateRunId(length=24):
    set = string.ascii_lowercase
    return ''.join(random.choice(set) for i in range(length))
