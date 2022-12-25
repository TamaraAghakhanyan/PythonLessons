r = range(10)
print(r)
print(type(r))

print(list(r)) #returns the range as a list type

#indexing
print(r[0])
print(r[-1])
print(r[3])

#verifying the element is or is not a member of a range
print(10 in r)
print(3 in r)
print(60 not in r)

#find index of element in range
print(r.index(4))

#you cannot slice a range,
#but you can convert a range to a list then you can use slice method
print(list(r)[2:5])
#Write code in between the parentheses of print() to print out the index of 30 in range(10, 100, 10).

r1 = range(10, 100, 10)

print(r1.index(30))