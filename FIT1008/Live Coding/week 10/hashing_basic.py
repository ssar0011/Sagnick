def runDayHash(day,tableSize):
    """
    if day.lower()=="mon":
        key = 0
    elif day.lower() == "tues":
        key = 1
    etc.
    """
    key = day
    return key % tableSize

tableSize = 7
runsHashTable = [None]*tableSize
#on monday we ran 2000
pos = runDayHash(0,tableSize)
runsHashTable[pos] = 2000

runsViaPython = dict()
runsViaPython["mon"]=2000

def date_of_birth_hash(date,tableSize):
    #use the year --> turn into days
    #turn month into days
    #add days
    days_from_year = 365*(date.year-1)
    days_from_month = 31*(date.month-1)
    key = date.day + days_from_month + days_from_year
    return key % tableSize

class date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year= year

    def __str__(self):
        return str(self.day)+"/"+str(self.month)+"/"+str(self.year)
dob_table_size = 5
dob_hash_table = [None]*dob_table_size

person = (date(10,12,1911),"greg")
person2 = (date(11,12,1911),"not greg")
person3 = (date(1,1,2000),"you?")
person4 = (date(30,12,1999),"someone else in the class?")
people = [person,person2,person3,person4]
for individual in people:
    hashedKey = date_of_birth_hash(individual[0],dob_table_size)
    print(date_of_birth_hash(individual[0],dob_table_size),individual[1])
    dob_hash_table[hashedKey] = individual[1]

print(dob_hash_table)