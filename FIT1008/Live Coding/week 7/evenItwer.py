class evenNums:
    def __init__(self,num):
        self.current = 0 # zero is an even number 
        self.stopPlsNoMore = num # the limit which we can't exceed

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stopPlsNoMore: #if value exceeds upper bound -> exit
            raise StopIteration
        else:
            value = self.current #goto next even number by adding 2
            self.current += 2
            return value

F = evenNums(25)
for even in F:
    print(even)

Test = evenNums(1)
for item in Test:
    print(item)
testEven = evenNums(4)

for item in testEven:
    print(item)

for item in evenNums(-5):
    print(item)