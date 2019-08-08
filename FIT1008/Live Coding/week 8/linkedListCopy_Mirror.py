from linkedList import linkedList
from linkedStack import node

def copy(self):
    return self._copy_aux(self.head,linkedList())

def _copy_aux(self,current,copyList):
    if current is None: # theres no more shit in the list homie
        return copyList
    else:
        value = current.value
        self._copy_aux(current.next, copyList) # first arg to advance us, current.next
        copyList.insert(value,0) # since its after the recursive call we add it to the start, if we add b4 the recursive call then we would add to the end 
        return copyList

def mirror(self):
    return self._mirror_aux(self.head, linkedList()) # for any given linked list i'll have a copy of that linked list

def _mirror_aux(self, current, copyList):
    if current is None: #how do I do it with just one copy of the middle element? spoilers,
        # I'll need two base cases to handle the empty case as well
        return copyList
    elif current.next is None:
        copyList.insert(current.value,0)
        return copyList
    else:
        value = current.value
        copyList.insert(value, 0) # insert both before and after recursive call to add the same value to the start and then end to creeate a mirror
        self._mirror_aux(current.next, copyList)
        copyList.insert(value, 0)
        return copyList

linkedList.copy = copy #adds a new method to the linkedlist class
linkedList._copy_aux = _copy_aux
linkedList.mirror = mirror
linkedList._mirror_aux = _mirror_aux

A = linkedList()
B = A.copy()
F = A.mirror()
print(A,B,F)
A.insert(1,0)
A.insert(2,0)
A.insert(3,0)
A.insert(4,0)
A.insert(5,0)
C = A.copy()
print(A,C)
C.getNode(2).value = "bad thing"
print(A,C)

D = A.mirror()
print(D)