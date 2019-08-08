class Node:
    def __init__(self,value,weight,link=None):
        self.value = value
        self.weight = weight
        self.next = link

    def __str__(self):
        return "{"+str([self.value,self.weight])+"}"

class linkedList:
    def __init__(self): # constructor
        self.head = None #where the list starts
        self.count = 0 #initially 0 items in list

    def __len__(self):
        return self.count # we dont have to figure out length

    def __str__(self):
        string = "List: ("+str(len(self))+") "
        current = self.head
        while not (current is None):
            string += " -> " + str(current)
            current = current.next
        string += ""
        return string

    def getNode(self,index): # get a node at a given position
        current = self.head
        if index >= len(self) or index < 0:
            raise StopIteration("Node doesn't exist at this index")
        currentPos = 0 # give ourself a starting point that advances when we move up
        while not current is None and currentPos<index: #while it isn't empty
            current = current.next #advance to next node
            currentPos += 1
        return current

    def insert(self,item,w,index): # put an item at an index of the list
        if index==0:
            self.head = Node(item,w,self.head)# if empty then head is next node
            # node(item,self.head) means head used to be there
        else:
            someNode = self.getNode(index-1) 
            someNode.next = Node(item,w,someNode.next) # points to the next node
        self.count+=1

    def delete(self,index):
        if index==0:
            self.head = self.head.next # if first item then change head to next item
        else:
            before = self.getNode(index - 1) # change its link by linking the node before with the next node of item we want to delete
            itemToRemove = before.next
            before.next = itemToRemove.next
        self.count-=1




aList = linkedList()
#aList.delete(1)
#aList.delete(0)
print(aList)
aList.insert("yeet",10,0)
print(aList)
aList.insert("boi",5,0)
print(aList)
aList.insert("awww snap",8,2)
print(aList)
aList.insert("awww snap2",69,len(aList)) # add to the end
print(aList)
'''
aList.insert("awww snap3",len(aList))
print(aList)
aList.delete(0)
aList.insert("awww snap4",len(aList))
print(aList)
aList.insert("middle man",3)
print(aList)
aList.delete(1)
print(aList)
aList.delete(len(aList)-1)
print(aList)
'''