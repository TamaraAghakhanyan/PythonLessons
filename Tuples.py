my_tuple = ()
print(type(my_tuple))

# creating a tuple with a single element; a comma must be written after it
my_tuple = (9,)
print(type(my_tuple))
print(my_tuple)

# tuples with more elements; tuples support indexing
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[3])
print(my_tuple[-2])
print(my_tuple[-1])

# since tuples are immutable you cannot add/remove/modify elements of the tuple
# my_tuple[1] = 10 TypeError: 'tuple' object does not support item assignment
# del my_tuple[1] TypeError: 'tuple' object doesn't support item deletion

# /tuple assignment: this means, you assign a tuple of variables to a tuple of values
# and map each variable to a corresponding value of second tuple; tuple packing and
# unpacking;
tuple1 = ('Cisco', '2600', '12.4')
print(tuple1)
(vendor, model, ios) = tuple1
print(vendor)
print(model)
print(ios)

# both tuples should heve the same number of elements:
#tuple2 = (1, 2, 3, 4)
#(x,y,z) = tuple2 ValueError: too many values to unpack (expected 3)
(a,b,c) = (10,20,30)
print(a)
print(b)
print(c)

#Tuples vs. Lists
#tuples - immutable, cannot be modified: add/remove/delete elements; have fixed length
#lists - mutable, can be modified: add/remove/delete elements; length can be changed
#tuples ()
#lists []

a = ()
b = []
print(type(a))
print(type(b))

print(dir(a)) #returns the methods which are available for a data type
print(dir(b)) #returns the methods which are available for a data type


#Tuples -methods

#finding out the nnumber of elements inside the tuple
tuple2 = (1,2,3,4)
print(tuple2)
print(len(tuple2))

print(max(tuple2))
print(min(tuple2))

print(tuple2 + (5,6,7))
print(tuple2*2)

print(tuple2)
print(tuple2[:2])
print(tuple2[:])
print(tuple2[:-1])
print(tuple2[::-1])
print(tuple2[-3:-2])
print(10 in tuple2)
print(1 in tuple2)
print(10 not in tuple2)
del tuple2
#print(tuple2) NameError: name 'tuple2' is not defined
my_tuple = (1, 2, 3, 'a', 'b', 'c', [4, 5, 6])
print(my_tuple[::2])