# python can print multiple values at the same time

x=1
y=5.789
z="hello"

print(x,y,z)

#global variables-- same as that in other languages

#global keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)