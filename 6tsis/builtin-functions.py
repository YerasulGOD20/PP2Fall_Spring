'''#1
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((8, 2, 3, -1, 7)))'''
'''#2
def string_test(s):
    a="QWERTYUIOPASDFGHJKLZXCVBNM"
    b="qwertyuiopasdfghjklzxcvbnm"
    n1=0
    n2=0
    for i in s:
        if i in a:
            n1+= 1
        else:
            n2+= 1
    print ("No. of Upper case characters : ", str(n1))
    print ("No. of Lower case Characters : ", str(n2))
s=input()
print(string_test(s))'''
'''#3
def checkk(string):
    if string == string[::-1]:
        print(True)
    else:
        print(False)
a=input()
print(checkk(a))'''
'''#4
import math
def sqrt(number):
    print(math.sqrt(number))
a=input()
print(sqrt(a))'''
'''#5
x = (True, True, False)
result = all(x)
print(result)'''