import random

def quicksort(the_list):
    return quicksort(the_list,0,len(the_list)-1)

def quicksort_aux(the_list,left,right):
    if right<=left:
        return #nothing to return, list is modified
    rand1 = random.randint(left,right)
    pivot = the_list[rand1] #better is middle of 3 or maybe 5 or maybe 1% of input size!
    position_of_pivot = partition(the_list,left,right,rand1)
    quicksort_aux(the_list,left,position_of_pivot-1)
    quicksort_aux(the_list,position_of_pivot+1,right)

def quicksort_old(the_list):
    if len(the_list):
        return the_list
    rand1 = random.randint(0, len(the_list)-1)
    pivot = the_list[rand1]  # better is middle of 3 or maybe 5 or maybe 1% of input size!
    left,right = partition_old(the_list,pivot)
    the_list[:] = left + [pivot] + right

def partition(the_list,left,right,pivot):
    # let k be the current item
    #[otherstuff,...,pivot,stuff smaller,...,stuff>=,stuff unlooked at, ...stuff after right]

def partition_old(the_list,pivot):
    left = []
    right = []
    pivotCount = 0
    for item in the_list:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            if pivotCount>0:
                right.append(item)
            pivotCount+=1

    return [left,right]

def testMergeSort():
    testCases = [[],[1],[5,2,4,3,1],[1,2,4,3],[6,5,4,1],["c","b","a"],[1,6,3,6,3,7,1]]
    testOutputs = [[],[1],[1,2,3,4,5],[1,2,3,4],[1,4,5,6],["a","b","c"],[1,1,3,3,6,6,7]]
    for testPos in range(len(testCases)):
        case = testCases[testPos]
        result = testOutputs[testPos]
        case = quicksort(case)
        assert case==result, "test "+str(testPos+1)+" failed (expected: "+str(result)+" and got: "+str(case)+")"


if __name__=="__main__":
    testMergeSort()