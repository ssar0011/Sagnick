def longest_pos_seq(the_list):
    """
    uses dynamic programming to find the longest positive sequence in the_list
    @:param the_list - a list of numbers
    @:raises nothing
    @:complexity O(n) best and worst
    @:pre none
    @:post none
    @:returns the start position and length of the longest positive
    """
    dp_solution = [0]*len(the_list)
    if the_list[0]>0: #initial case for the start of the list
        dp_solution[0] = 1

    for i in range(1,len(the_list)):
        if the_list[i] > 0:
            dp_solution[i] = 1 + dp_solution[i-1] #if extending and no sequence to the left, we'd add 0 anyway which is safe
        else:
            dp_solution[i] = 0


    maxLen = dp_solution[0]
    bestPos = 0
    for pos in range(len(the_list)):
        if dp_solution[pos] > maxLen:
            maxLen = dp_solution[pos]
            bestPos = pos
    if maxLen == 0: #arbitrary where starts when no seq
        start = 0
    else:
        start = bestPos - (maxLen-1)
    return [start,maxLen]

def max_subseq_sum(the_list):
    """
    description here: uses DP to find the maximum subarray sum
    @:param the_list: the list to find the maximum subarray sum within (reals only pls)
    @:raises none
    @:complexity ????
    @:pre none
    @:post none
    @:returns [start,value] of maximum sum subarray
    """
    dp_solution = [None] * len(the_list)

    dp_solution[0] = the_list[0]

    for i in range(1, len(the_list)):
        withSeq = dp_solution[i-1] + the_list[i] # if the item to the left is positive then we want to extend
        withoutSeq = the_list[i]
        dp_solution[i] = max(withoutSeq,withSeq)

    ###
    bestStart = len(the_list)-1
    bestSum = dp_solution[len(the_list)-1]
    bestEnd = len(the_list)-1
    currentSum = bestSum
    pos = len(the_list)-2
    while pos >= 0:
        if dp_solution[pos] > bestSum:
            bestSum = dp_solution[pos]
            bestEnd = pos
            currentSum = bestSum
        if dp_solution[pos] < 0:
            if currentSum == bestSum:
                bestStart = pos+1
            currentSum = dp_solution[pos]
        pos -=1
    if dp_solution[0]>0 and currentSum==bestSum:
        bestStart=0
    #todo find where max sum occurs
    return [bestStart,bestSum]

def testlongseq():
    cases = [[0,0,0,0,0],[-1,-4,-22,-2,-1],[1,2,3,4,5],[1,2,-1,5]]
    outputs = [[0,0],[0,0],[0,5],[0,2]]
    for testNum in range(len(cases)):
        expect = outputs[testNum]
        actual = longest_pos_seq(cases[testNum])
        assert (actual==expect), "test "+str(testNum)+" failed -- expected: "+str(expect)+" got: "+str(actual)

def testmaxseqsum():
    cases = [[0, 0, 0, 0, 0], [-1, -4, -22, -2, -1], [1, 2, 3, 4, 5], [1, 2, -1, 5],[90,90,0,-200,1,2,96,-1,-100,99,0,0,-5,-7,-9,25],[1,2,0,-4,1,2,96,-1,-100,99,0,0,-5,-9,-7,25]]
    outputs = [[4, 0], [4, -1], [0, 15], [0, 7],[0,180],[9,103]]
    for testNum in range(len(cases)):
        expect = outputs[testNum]
        actual = max_subseq_sum(cases[testNum])
        print("test "+str(testNum)+" passed:",(actual==expect)," expected: "+str(expect)+" got: "+str(actual))

if __name__=="__main__":
    testlongseq()
    testmaxseqsum()