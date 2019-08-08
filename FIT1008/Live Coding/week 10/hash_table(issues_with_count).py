from referential_array import build_array
def date_of_birth_hash(date,tableSize):
    #use the year --> turn into days
    #turn month into days
    #add days
    days_from_year = 365*(date.year-1)
    days_from_month = 31*(date.month-1)
    key = date.day + days_from_month + days_from_year
    return key % tableSize

class kv_pair:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return "("+str(self.key)+","+str(self.value)+")"

class hash_table:
    def __init__(self,tableSize=31):
        self.array = build_array(tableSize)
        self.tableSize = tableSize
        self.count = 0

    def __str__(self):
        string = ""
        for index in range(self.tableSize):
            if self.array[index] is None:
                pass
            else:
                string += str((index,str(self.array[index])))
                string += ","
        return string

    def __setitem__(self, key, value):
        self.array[self.linear_probe(key)]=kv_pair(key,value)
        self.count+=1 #UPDATE THIS - should not change for an overwrite! we will discuss this in the wednesday lecture!

    def __getitem__(self, instance, owner):
        pass

    def hash_value(self,key):
        return date_of_birth_hash(key,self.tableSize)

    def linear_probe(self,key,sneakykey = None):
        """

        :param self:
        :param key: the key to place something using
        :return: the location in the table for it to go
        :raise: index error where not possible
        """
        if self.count == self.tableSize:
            raise IndexError("hash table is full!")
        if not sneakykey is None:
            hashv = sneakykey
        else:
            hashv = self.hash_value(key)  # first try
        pos = hashv
        while not (self.array[pos] is None or self.array[pos].key == key):
            pos = (pos +1)%self.tableSize
        return pos

class date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return str(self)==str(other)

    def __str__(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)
person = (date(10,12,1911),"greg")
person2 = (date(11,12,1911),"not greg")
person3 = (date(1,1,2000),"you?")
person4 = (date(30,12,1999),"someone else in the class?")
people = [person,person2,person3,person4]
people.append((date(10,12,1911),"also not greg, please replace greg"))
people.append((date(1,1,2000),"you?"))
people.append((date(2,10,2018),"baby"))
people.append((date(2,12,2018),"baby"))
people.append((date(2,7,2018),"baby"))
people.append((date(2,4,2018),"baby"))
dob_hash_table = hash_table(7)
for individual in people:
    dob_hash_table[individual[0]] = individual[1]

#print(dob_hash_table)
#print(dob_hash_table.linear_probe("silly",5))

print(dob_hash_table)