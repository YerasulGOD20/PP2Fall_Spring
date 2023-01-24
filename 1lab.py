'''
print("Hello, World!")
'''
'''
if 6 > 2:
 print("Six is greater than two!") #this code answer to which number is bigger
'''
'''
x=5
y=5
print(x+y) #This code is about x plus y
'''
'''
x = 5
y = "Kennedy" 
print(x)
print(y) #This code about the printing just variables
'''
'''
x = 5
myvar = "John"
print(int(x))
print(str(myvar))
'''
'''
x = y = z = "Orange"
print(x)
print(y)
print(z)
'''
'''
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
'''
'''
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
'''
'''
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
'''
'''
x = 1    # int
y = 2.8  # float
z = 1j   # complex
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
'''
'''
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
'''
'''
a = "Hello, World!"
print(a[1])
'''
'''
for x in "banana":
  print(x)
'''
'''
a = "Hello, World!"
print(len(a))
'''
'''
txt = "The best things in life are free!"
print("expensive" not in txt)
'''
'''
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
'''
'''
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
'''
'''
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
'''
'''
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
'''
'''
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
'''
'''
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
'''