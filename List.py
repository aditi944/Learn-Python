# Lists are used to store multiple items in a single variable.

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List items are ordered, changeable, and allow duplicate values.

#length of list

print(len(thislist))

# -1 refers to the last element, and the counting goes backward

# to check if a certain element lies in the list

if "apple" in thislist:
    print("present")
    
else:
    print("absent")
    
#change items
thislist[1]="mango"
print(thislist)

# to insert new items without removing the previous ones- insert()- it inserts at a particular position

thislist.insert(2,"watermelon")
print(thislist)

# extend()-To append elements from another list to the current list

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# remove elements- 1. specific element- remove()

thislist.remove("cherry")

#pop()- removes the specific index

thislist.pop(1)
print(thislist)

# clear list
# thislist.clear()
# print(thislist)

# loop through a list

for x in thislist:
    print(x)
    
print("hello")
for i in range(len(thislist)):
    print(thislist[i])
    
# list comprehension- when you have to create a new list based upon the previous ones
# syntax- newlist = [expression for item in iterable if condition == True]

newlist = [x for x in thislist if x != "apple"]
print(newlist)

# sort list in ascending order

print(thislist.sort())

new=[20,10,7,89]
new.sort()
print(new)

# sort list in descending list

new.sort(reverse = True)

# list methods


# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list