dict1 = {}
print(dict1)
print(type(dict1))
dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
print(dict1)

#accessing the elementsq of dictionary, by specifying accociated key for the value we
#want to extract
print(dict1["IOS"])
print(dict1["Vendor"])

#adding new value to the dictionary
dict1["RAM"] = "128"
print(dict1)

#modifying the value inside the dictionary
dict1["IOS"] = "12.3"
print(dict1)

#deleting a pair from the dictionary
del dict1["Ports"]
print(dict1)

#find out the number of key values inside the dictionary
print(len(dict1))

#to verify if cetain sting is a key or not in the dictionary
print("IOS" in dict1)
print("IOS"not in dict1)

#used to obtain a list having the keys/values in the dictionary as elements
print(dict1.keys())
print(dict1.values())

#returns list of tuples each of which containing the key and the value
print(dict1.items())

#checking the type of dict1.keys()
print(type(dict1.keys()))

#checking the type of dict1.values()
print(type(dict1.values()))

#checking the type of dict1.items()
print(type(dict1.items()))

#access the list returned by dict1.keys()
print(list(dict1.keys()))

#access the list returned by dict1.values()
print(list(dict1.values()))

#access the list returned by dict1.items()
print(list(dict1.items()))

