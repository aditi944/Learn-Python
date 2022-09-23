# strings can be surrounded by single qoutes or double quotes

# multiple strings is surrounded by 3 quotes

#in python, string can be considered as arrays of characters

#looping through a string

for x in"bababa":
    print(x)
 
x="hello idiot"   
#string length
print(len(x))

#to scheck if any string or char is present in another string

txt="hello, this is aditi jha {}"
if "adii" in txt:
    print("present")
    
else:
    print("not present")
    
#slicing-- you can return a range of characters by using the slice syntax

print(txt[2:10])

#modify strings
# lower() coverts to lowercase
# upper() converts to uppercase
# strip() removes any whitespace from the beginning or the end
# replace() replaces a string with another one- a.replace()

print(txt.replace("a", "p"))
# print(txt)

# in python, strings can be concatenated but we can not concat string with other data types. For this purpose, format() is used

a=5
print(txt.format(a))

#escape character- used to include illegal strings, for example- "viking"

s="hello we are so called \"phoebe\""

print(s)