class JustCounter:
    __setcounter=0
    def count(self):
        self.__setcounter+=1
        print(self.__setcounter)
counter=JustCounter()
counter.count()
counter.count()
print(counter._JustCounter__setcounter)
-------------------------------------------------------------------------------------
'''def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b
fibb = fibonacci()
for i in range(12):
  print(next(fibb), end=' ')'''
'''def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield (n ** 2) 
        n += 1
x=PowTwoGen(6)
for i in range(1,7):
    print(next(x),end=' ')'''
4. Pipelining Generators
Generators can be used to pipeline a series of operations. This is best illustrated using an example.

Suppose we have a log file from a famous fast food chain. The log file has a column (4th column) that keeps track of the number of pizza sold every hour and we want to sum it to find the total pizzas sold in 5 years.

Assume everything is in string and numbers that are not available are marked as 'N/A'. A generator implementation of this could be as follows.

with open('sells.log') as file:
    pizza_col = (line[3] for line in file)
    per_hour = (int(x) for x in pizza_col if x != 'N/A')
    print("Total pizzas sold = ",sum(per_hour))
This pipelining is efficient and easy to read (and yes, a lot cooler!).
Python Enhancement Proposal.