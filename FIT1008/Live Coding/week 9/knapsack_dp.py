def knapsack_dp(values,weights,max_cap):
    """
    uses DP to solve the knapsack problem for params given
    :param values: the values of items available
    :param weights: the weights of items available
    :param max_cap: the maximum capacity (integer, pls not too huge)
    :return: returns the matrix holding optimal value (can be backtracked to identify contents)
    """
    #for c and k, dp is better of c,k-1 and c-weight(k),k-1 + value(k)
    item_count = len(weights)
    dp_knap_sol = [None]*(item_count+1)
    for given_item in range(item_count+1):
        dp_knap_sol[given_item] = [0]*(max_cap+1)
    #generate 2d array to hold results
    #initial conditions
    for item in range(item_count+1):
        dp_knap_sol[item][0] = 0 #value 0 if no capacity
    for cap in range(max_cap+1):
        dp_knap_sol[0][cap] = 0 #no items, no value
    dp = dp_knap_sol
    for curritem in range(1,item_count+1):
        for currcap in range(1,max_cap+1):
            no_use_it = dp[curritem-1][currcap]
            how_heavy = weights[curritem-1]
            dollar = values[curritem-1]
            reduced_cap = currcap-how_heavy
            if reduced_cap >= 0: #we have room
                use_it = dp[curritem-1][reduced_cap]+dollar
            else:
                use_it = 0 #don't use me!!! I am too big
            best = max(no_use_it,use_it)
            dp[curritem][currcap] = best
        #use knapsack relation
    return dp_knap_sol #to move into excel to backtrack

def neat_str_table_to_tsv(table,header=False):
    output = ""
    line = ""
    if header:
        line = '\t'
        for pos in range(len(table[0])):
            line+=str(pos)
            line+='\t'
        line = line[:-1]
    output+=line+'\n'
    pos=0
    for inner in table:
        line = ""
        if header:
            line = "|"+str(pos)+'|'+'\t'
        for item in inner:
            line+=str(item)
            line+='\t'
        line = line[:-1]
        output+=line+"\n"
        pos+=1
    return output


def testKnap():

    vals = [1,2,3,9]
    weights = [1,20,100,4]
    print(neat_str_table_to_tsv(knapsack_dp([20], [1], 1),True)) #only one item to use, fits, is selected for 20 value 1 weight
    print(neat_str_table_to_tsv(knapsack_dp([20,21], [1,5], 1),True)) #two items, one doesn't fit cap 1 (non-square dp sol of minimal size) value 20, weight 1
    print(neat_str_table_to_tsv(knapsack_dp(vals,weights,20),True)) #2,20 possible but not used, 1,1 and 9,4 best for value 10, weight 5
    print(neat_str_table_to_tsv(knapsack_dp(vals, weights, 19),True)) #2,20 not possible but 1,1 and 9,4 is; value = 10;weight5
    print(neat_str_table_to_tsv(knapsack_dp(vals, weights, 99),True)) #all but 3,100 possible, best choice to use all for value of 12
    print(neat_str_table_to_tsv(knapsack_dp(vals, weights, 100),True)) #3,100 possible but less than value of others, don't use 3,100 for value of 12

if __name__=="__main__":
    testKnap()