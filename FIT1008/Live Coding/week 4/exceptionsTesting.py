
def F1():
    try:
        aList = [1,3,5]
        print(1**5)
        print(aList[2])
        print(20/0)
        print(aList[1])
    
    
def f2():
    F1()

f2()


def div(a,b):
    assert b != 0
    return a/b
    
print(div(1,5))
print(div(6,0))


def rollingBufferAverage(oldAv,oldList,newList,direct):
    assert len(oldList)>0 and len(newList)>0 , "doesn't work with empty lists"
    assert type(direct)==type("hi!"),"direction must be a string"
    assert direct == "right" or direct == "left","only right or left as directions"
    newAv = oldAv
    if direct == "right":
        newAv -= oldList[-1]
        newAv += newList[0]
    else:
        newAv -= oldList[0]
        newAv += newList[-1]
    return newAv
    
print(rollingBufferAverage(10,[1,2,3,4],[2,3,4,5],"left"))
print(rollingBufferAverage(10,[1,2,3,4],[2,3,4,5],"RIGHT"))
