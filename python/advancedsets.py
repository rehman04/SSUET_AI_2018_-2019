s=set()
s.add(1)
print(s)
s.add(2)
print(s)
s.clear()
print(s)
s={1,2,3}
sc=s.copy()
s.add(4)
print(sc)
print(s.difference(sc))
-----------------------
s1={1,2,3}
s2={1,4,5}
s1.difference_update(s2)
print(s1)
print(s2)
s2.discard(4)
print(s2)
------------------------------
s1={1,2,3}
s2={1,2,4}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
---------------------------------
s1={1,2,3}
s2={1,2}
s3={5}
print(s1.isdisjoint(s3))
--------------------------------
s1={1,2,3}
s2={1,2}
s3={5}
print(s1.isdisjoint(s3))
print(s2.issubset(s1))
print(s2.issuperset(s1))
print(s1.symmetric_difference(s2))
print(s1.union(s2))
s2.update(s1)
print(s2)
