from linkedList import linkedList

class linkedListIterator:
    def __init__(self,the_list): # set it up so ur looking at 1st item  
        assert type(the_list)==type(linkedList())
        self.whereAmI = the_list.head # start at the head and go though one at a time

    def __iter__(self):
        return self # all we want is smth iterable

    def __next__(self):
        if self.whereAmI is None:
            raise StopIteration
        returnedValue = self.whereAmI.value
        self.whereAmI = self.whereAmI.next
        return returnedValue