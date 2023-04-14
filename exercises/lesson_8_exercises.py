"""
Exercise 1: Below are the two lists convert it into the dictionary.
"""

# keys = ["Ten", "Twenty", "Thirty"]
# values = [10, 20, 30]
#
# dict = dict(zip(keys, values))
# print(dict)




"""
Exercise 2:
Access the value of key "history" from the below dict
"""
sampleDict = {
    "class":
        {"student":
             {"name": "Mike",
              "marks":
                  {"physics": 70, "history": 80}}}
}

print(sampleDict['class']['student']['marks']['history'])





"""
Exercise 3:
Create a new dictionary by extracting the following keys from a below dictionary
"""
sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
# Keys to extract
# keys = ["name", "salary"]

# Expected output: {'name': 'Kelly', 'salary': 8000}

del sampleDict["age"]
del sampleDict["city"]
print(sampleDict)
"""
Exercise 4:
Slice list into 3 equal chunks and reverse each chunk
"""
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunked_list = []
chunk_size = 3

for i in range(0, len(sample_list), chunk_size):
    chunked_list.append(sample_list[i: i + chunk_size])

print((chunked_list[::-1]))



"""
Exercise 5:
Write a program to iterate a given list and count
the occurrence of each element and create a dictionary 
to show the count of each element.
"""
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

# Expected Outcome: Printing count of each item  {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

count = []
list1 = []
for i in sample_list:
    a = sample_list.count(i)
    if i in list1 or a in count:
        continue
    else:
        list1.append(i)
        count.append(a)

print(count)
print(list1)


"""
Exercise 6:
Sort the list items by accending order without using list special methods like 'sort()'.
"""

my_list = [5,8,1,6,4,9,7,2,3]




