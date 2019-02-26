'''python debugger module
timeit (python built in Magic function)'''
import timeit
s='1-2-3-4-....-99'
print(s)
x=timeit.timeit('"-".join(str(n) for n in range(100)) ',number=10000)
print(x)
t=timeit.timeit('"-".join([str(n) for n in range(100)]) ',number=10000)
print(t)
m=timeit.timeit('"-".join(map(str,range(100))) ',number=10000)
print(m)
#%timeit("-".join(str(n) for n in range(100)))
#%timeit("-".join([str(n) for n in range(100)]))
#%timeit("-".join(map(str,range(100))))