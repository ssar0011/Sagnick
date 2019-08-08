def swap(the_list,pos1,pos2):
    tmp = the_list[pos1]
    the_list[pos1] = the_list[pos2]
    the_list[pos2] = tmp

def bubbleSort(aList):
    sorted = False
    while not sorted:
        sorted = True
        for pos in range(len(aList)-1):
            if aList[pos] > aList[pos+1]:
                swap(aList,pos,pos+1)
                sorted = False

def insertionSort(aList):
    #expand sorted section
    for Mark in range(len(aList)):
    #Mark for item to shift back
        pos = Mark
        while pos > 0 and aList[pos-1] > aList[pos]:
            
            swap(aList,pos-1,pos)
            pos -= 1
        #shift item backwards

aList = [1,2,3,4,5]
bList = [5,4,3,2,1]
cList = [1,2,3,4,3,2,1]
dList = [4,3,2,1,2,3,4]

insertionSort(aList)
insertionSort(bList)
insertionSort(cList)
insertionSort(dList)

print(aList)
print(bList)
print(cList)
print(dList)


