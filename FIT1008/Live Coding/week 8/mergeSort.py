def mergeSort(the_list):
    copy =[0]*len(the_list)
    mergeSortAux(the_list,0,len(the_list)-1,copy)

def mergeSortAux(the_list,left,right,copy):
    if left < right:
        mid = (left+right)//2
        mergeSortAux(the_list,left,mid,copy)
        mergeSortAux(the_list,mid+1,right,copy)
        mergeArray(the_list,copy,left,right)

    else:
        pass #who cares, no list to do stuff with
    #raise NotImplementedError

def mergeArray(the_list,listCopy,left,right):
    copyPos = 0
    lPoint = left
    mid = (left+right)//2
    rPoint = mid+1
    while lPoint < mid+1 and rPoint < right+1:
        if the_list[lPoint] < the_list[rPoint]:
            listCopy[copyPos] = the_list[lPoint]
            lPoint += 1
        else:
            listCopy[copyPos] = the_list[rPoint]
            rPoint += 1
        copyPos += 1
    while lPoint < mid + 1:
        listCopy[copyPos] = the_list[lPoint]
        copyPos += 1
        lPoint+=1
    while rPoint < right+1:
        listCopy[copyPos] = the_list[rPoint]
        copyPos += 1
        rPoint += 1

    takeFromCopy = 0
    for theListPos in range(left,right+1):
        the_list[theListPos] = listCopy[takeFromCopy]
        takeFromCopy+=1


def testMergeSort():
    testCases = [[],[1],[5,2,4,3,1],[1,2,4,3],[6,5,4,1],["c","b","a"],[1,6,3,6,3,7,1]]
    testOutputs = [[],[1],[1,2,3,4,5],[1,2,3,4],[1,4,5,6],["a","b","c"],[1,1,3,3,6,6,7]]
    for testPos in range(len(testCases)):
        case = testCases[testPos]
        result = testOutputs[testPos]
        mergeSort(case)
        assert case==result, "test "+str(testPos+1)+" failed (expected: "+str(result)+" and got: "+str(case)+")"


if __name__=="__main__":
    testMergeSort()