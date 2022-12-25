#craeting a set
list4 = [1, 2, 3, 4, 5, 2, 3]
print(list4)
print(set(list4))
set1 = set([11, 12, 13, 14, 15, 15, 15, 11])
print(set1)
print(type(set1))

set2 = {11, 12, 13, 14, 15, 15, 15, 11}
print(set2)
print(type(set2))

print(len(set2))

#checking whether an element is or is not a membet of a set
print(11 in set2)
print(10 in set2)
print(10 not in set2)

#adding an element to the set
print(set2)
set2.add(16)
print(set2)

#remove an element from a set
set2.remove(11)
print(set2)

#Sets - Methods and Operations

set1 = {1, 2, 3, 4}
print(set1)

set2 = {3, 5, 8}
print(set2)

#identify common elements of two sets
print(set1.intersection(set2))
print(set2.intersection(set1))

#returns not common elements of two sets
print(set1.difference(set2))
print(set2.difference(set1))

#unify two sets
print(set1.union(set2))

#removing a random element from a set
print(set1)
set1.pop()
print(set1)

#clear a set
set1.clear()
print(set1)

#Frozenseets

list1 = [1, 2, 3, 4]
list2 = [3, 4, 7]

fs1 = frozenset(list1)
fs2 = frozenset(list2)

print(fs1)
print(fs2)

print(type(fs2))

#add/remove an element
#AttributeError: 'frozenset' object has no attribute 'add'
#AttributeError: 'frozenset' object has no attribute 'remove'

#identify common elements of two frozensets
print(fs1.intersection(fs2))
print(fs2.intersection(fs1))

#returns not common elements of two sets
print(fs1.difference(fs2))
print(fs2.difference(fs1))

#unify two frozensets
print(fs1.union(fs2))
