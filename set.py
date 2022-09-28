# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
  print(x)
  
  #once a set is created, items cannt be changed but can be added
  
thisset.remove("banana");

print(thisset)