from linkedStack import node
class linkedQueue:
    def __init__(self):
        self.front = None # initially it is empty
        self.rear = None
        self.count = 0 # initially the number of items is zero

    def __str__(self):
        string = "Queue: Front: "
        current = self.front
        while not (current is None):
            string += " -> " + str(current)
            current = current.next
        string += " <- Rear"
        return string

    def append(self,item):
        the_node = node(item)
        if self.front is None: # if the queue is empty then they'll point to same thing
            self.front = the_node
            self.rear = the_node
        else:
            self.rear.next = the_node # next element 
            self.rear = self.rear.next # update rear or else elements will be floating in memory
        self.count+=1

    def serve(self):
        if self.count>0: #if count is positive then do stuff else queue empty
            itemServed = self.front.value # front points to current front item
            self.front = self.front.next # now front points to next item after serving
            self.count-=1
            return itemServed
        else:
            raise StopIteration("Queue is empty")

def testLinkedQueue():
    Q = linkedQueue()
    Q.serve() #expecting a crash bc can't serve from empty
    Q.append(1) #append to empty -> [1]
    print(str(Q),"expected [1]")
    Q.append(2)
    print(Q)
    Q.append(3)
    print(str(Q),"Expected [1,2,3]")
    print(str(Q.serve()),str(Q),"expected: [2,3]")
testLinkedQueue()