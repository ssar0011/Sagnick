def selectionSort(aList):
    """
    sorts the list as per selection sort
    @param: aList - a list of numbers
    precondition: none
    postcondition: aList is sorted
    @complexity: tbc
    """
    for swapTo in range(len(aList)):
        minP = swapTo
        for candidateMin in range(swapTo,len(aList)):
            item = aList[candidateMin]
            if item < aList[minP]:
                minP = candidateMin
        
        tmp = aList[swapTo]
        aList[swapTo] = aList[minP]
        aList[minP] = tmp
