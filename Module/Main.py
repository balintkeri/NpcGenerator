import NPCGenerator.Module.Randoms as Random

class NPC:
    def __init__(self, birthDay, firstname, lastname, nationality, gender):
        self.birthday = birthDay
        self.firstname = firstname
        self.lastname = lastname
        self.nationality = nationality
        self.gender = gender
        self.password = Random.getPassword()
        self.emailBody = self.lastname + "_"+ self.firstname + Random.getNumber(2)
        self.randomWord = Random.getWord()

    def getAge(self):
        pass

class Generator:
    def __init__(self):
        self.npcs = []

    def createRandom(self, nationality = Random.getNationality()):
        
        birthDay = Random.getBirthDate()
        gender = Random.getGender()
        firstname = Random.getFirstname(gender, nationality=nationality)
        lastname = Random.getLastname(nationality=nationality)
        
        newNPC = NPC(birthDay,firstname,  lastname, nationality, gender)
        self.npcs.append(newNPC)

        return self.npcs[-1]
        
    
