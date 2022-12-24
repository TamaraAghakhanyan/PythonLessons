list1 = []
print(type(list1))
list1 = ['Cisco', 'Juniper', 'Avaya', 10, 10.5, -11]
print(list1)

print(len(list1))  #returns the count of the elements in the list

print(list1[0]) #returns the element of the mentioned index
print(list1[-1]) #returns the last element of the list
print(list1[4])
print(list1[5]) #in case there is no element for the mentioned index, IndexError: list index out of range

#replacing an element in the list
print(list1)
print(list1[2])
list1[2] = 'HP'
print(list1)

#List Methods

#Finding the maximum/minimum value in the list
list2 = [-11, 2, 12]
print(list2)
print(max(list2))
print(min(list2))

#print(max(list1)) TypeError: '>' not supported between instances of 'int' and 'str'

list3 = ['a', 'b', 'c']
print(list3)
print(max(list3))

#appending a new element to the list, the new element is added at the end of the list
print(list1)
list1.append(100)
print(list1)

#3ways of removing an element from the list

del list1[4] #deletes an element at a specified index number in the list
print(list1)

print(list1.pop(0)) #returns the removed element from the list
print(list1)

list1.remove('Juniper') #removes the first matching value from the list
print(list1)

#inserting an element at a particular index
list1.insert(2, 'Nortel')
print(list1)

#appending a list to another list
list4 = [9, 99, 999]
print(list4)
print(list1)
list1.extend(list4)
print(list1)

#finding the index of the element in the list
print(list1.index(-11))

#returns the count of the element inside the list
list1.append(10)
print(list1)
print(list1.count(10))

#sorting the elements inside the list

#sorting the elemnts with the acsending order
list4.append(1)
list4.append(25)
list4.append(500)
print(list4)

list4.sort()
print(list4)

#sorting the elemnts with the reverse or decsending order
list4.reverse()
print(list4)

sorted(list4) #returns a new sorted list
print(list4)
print(sorted(list4, reverse=True))

help(sorted) #Return a new list containing all items from the iterable in ascending order.
    #A custom key function can be supplied to customize the sort order, and the
    #reverse flag can be set to request the result in descending order

#concatinating the lists
print(list1 + list4)
print(list3 * 3)

#List Slicing
list3 = [1,2,3,'a','b','c']
print(list3)
print(list3[0:3]) #extracting the 1st 3 element of the list
print(list3[2:5])
print(list3[:3]) #extracting the 1st 3 element of the list(not specifying the 1st index)
print(list3[2:]) #extracts the elements starting from the specified index til the end
print(list3[:]) #extracts all the elements of the list

#Slicing using negative indexes
print(list3[-1]) #returns the last element of the list
print(list3[-4:-1])
print(list3[-3:]) #slicing last 3 elements of the list
print(list3[:-3]) #slicing the elements of the list withount last 3 elements of the list
print(list3[::2]) #skiping every second element in the list using a step
print(list3[::-1]) #slicing the list elements in reverse order using a step
