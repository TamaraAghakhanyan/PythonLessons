# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
# to solve after lambda

# 2. Write a Python script to add a key to a dictionary.

dict = {0: 10, 1: 20}
dict[2] = 30
print(dict)

# 3. Write a Python script to concatenate following dictionaries to create a new one.
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Sample Dictionary :

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

# Solution1
dic1.update(dic2)
print(dic1)
dic1.update(dic3)
print(dic1)

# Solution2
dic4 = {}

for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)


# 4. Write a Python script to check whether a given key already exists in a dictionary.
dic1={1:10, 2:20}

print(1 in dic1)