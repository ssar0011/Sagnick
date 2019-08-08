def iterFact(n):
    factors = []
    for num in range(1,n+1):
        if n%num==0:
            factors.append(num)
    return factors

def tFactor(n):
    return tFactor_Aux(n,1,[])

def tFactor_Aux(n,index,currentFactors):
    if index==n:
        return currentFactors+[n]
    else:
        factorToInclude = []
        if n % index == 0:
            factorToInclude = [index]
        return tFactor_Aux(n,index+1,currentFactors+factorToInclude)

def uFactor(n,index=1):
    if index==n:
        return [index]
    else:
        factorToInclude = []
        if n%index==0: # check if it is a factor 
            factorToInclude = [index]
        return factorToInclude+uFactor(n,index+1) # whatever you do to the return value you do the same to the argument for tail recursive

def bFactor(n):
    return bFactorAux(n,1,n)

def bFactorAux(n,left,right):
    if left > right: # if pointers cross then its no there
        return []
    mid = left+right
    mid = mid//2
    factorToInclude = []
    if n % mid == 0:
        factorToInclude = [mid]
    return bFactorAux(n,left,mid-1) + factorToInclude + bFactorAux(n,mid+1,right)

print(tFactor(20),str([1,2,4,5,10,20]))
print(uFactor(20),str([1,2,4,5,10,20]))
print(bFactor(20),str([1,2,4,5,10,20]))