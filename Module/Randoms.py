import os
import random
import requests
import datetime
import secrets

WORKDIR = os.path.split(__file__)[0]


FIRSTNAMES_PATH = WORKDIR+ "\\Resources\\firstnames.csv"
LASTNAMES_PATH  = WORKDIR+ "\\Resources\\lastnames.csv"

NPC_AGE_MIN = 21
NPC_AGE_MAX = 50

WORD_LIST_PATH = "https://www.mit.edu/~ecprice/wordlist.10000"


def getPassword():
    return secrets.token_urlsafe(32)
    
def getMITwordList():
    response = requests.get(WORD_LIST_PATH)
    return response.content.splitlines()

WORDS = getMITwordList()

def getWord():
    word =  WORDS[random.randrange(0, len(WORDS))].decode("utf-8")
    return word

def getNumber(lenght = 3):
    number = random.randrange(0, 10**lenght)
    string = str(number)
    return string.zfill(lenght)

def getBirthDate( age = None,  ageMin = NPC_AGE_MIN, ageMax = NPC_AGE_MAX):
    now = datetime.datetime.now()
    if not age:
        maxYear = now.year - min(ageMin, ageMax)
        minYear = now.year - max(ageMin, ageMax)
        year = random.randrange(minYear, maxYear)
    else:
        year =  now.year - age
    month = random.randrange(1,12)
    day = random.randrange(1,28) #TODO
    return datetime.datetime(year, month, day)

def getGender():
    gender = random.randrange(0,2)
    match gender:
        case 1:
            return "female"
        case 0:
            return "male"
        

def getNames(path):
    with open(path, "r") as f:
        rawData = f.read()
    return rawData.split("\n")[1:]
    
def _getFirstNames():
    names = {
        "female" : {},
        "male" : {}
    }
    for line in getNames(FIRSTNAMES_PATH):
        nationality = line.split(";")[0]
        name        = line.split(";")[1]
        gender      = line.split(";")[2]

        if nationality not in names[gender].keys():
            names[gender][nationality] = []

        names[gender][nationality].append(name)

    return names

def _getLastNames():
    names = {}
    for line in getNames(LASTNAMES_PATH):
        nationality = line.split(";")[0]
        name        = line.split(";")[1]

        if nationality not in names.keys():
            names[nationality] = []

        names[nationality].append(name)

    return names



def _getNationalities():
    nationalities = []

    lastname = []
    for line in getNames(LASTNAMES_PATH): 
        nationality = line.split(";")[0]
        if nationality not in lastname:
            lastname.append(nationality)

    firstname = []
    for line in getNames(FIRSTNAMES_PATH):
        nationality = line.split(";")[0]
        if nationality not in firstname:
            firstname.append(nationality)

    for nationality in firstname:
        if nationality in lastname:
            nationalities.append(nationality)

    return nationalities
        
FIRSTNAMES = _getFirstNames()

LASTNAMES = _getLastNames()

NATIONALITIES = _getNationalities()

def getNationality():
    return NATIONALITIES[random.randrange(0,len(NATIONALITIES))]

def getFirstname(gender, nationality ):
    return FIRSTNAMES[gender][nationality][random.randrange(0,len(FIRSTNAMES[gender][nationality]))]
    

def getLastname(nationality ):
    return LASTNAMES[nationality][random.randrange(0,len(LASTNAMES[nationality]))]