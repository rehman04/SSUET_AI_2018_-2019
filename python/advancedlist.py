'''l=[1,2,3]
l.append([4,5])
print(l)
l.remove(l[3])
l.extend([4,5])
print(l)
l.insert(2,'inserted')
print(l)
l.reverse()
print(l)'''
#Test
print(hex(1024))
print(bin(1024))
#--------------------------
print(round(5.23222,2))
#-------------------------
s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())
p = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(p.count('w'))
#----------------------
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))
#------------------------------------
print(set1.union(set2))
#----------------------------------
print({x:x**3 for x in range(5)})