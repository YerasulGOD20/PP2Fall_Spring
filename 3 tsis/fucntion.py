'''def grams(x):
    return 28.3495231*x

gramss = 10
ounces=grams(gramss)
print(ounces)
'''
'''
def afd(F):
    return (5.0/9.0) * (F - 32)
F=80
c=afd(F)
print(c)
'''
'''
def opas(heads, legs):
    for i in range(heads + 1):
        j = heads - i
        if 2 * i + 4 * j == legs:
            return i, j
heads = 35
legs = 94
solution = opas(heads, legs)
print (solution)
'''

'''
def sex(products):
    for i, v in products.items():
        if len(i) >= 4:
            print(v)


def sex1(products):
    for i in products:
        if len(i) >= 4:
            print(products[i])


products = {"name": "SAM", "country": "KZ", "age": "20", "number": "4578"}

sex(products)
print(" ")
sex1(products)

print(products["name"])
'''
'''
def printperm(string):
    if len(string) == 1:
        return [string]
    perms = printperm(string[1:])
    char = string[0]
    res = []
    for i in perms:
        for j in range(len(i) + 1):
            res.append(i[:j] + char + i[j:])

    return res

print(printperm("abc"))
'''
'''
def reverse(word):
    print(word[::-1])

reverse("we are studying")
'''
'''
def check(list):
    for i in range(len(list) - 1):
        if list[i] == 3 and list[i + 1] == 3:
            return True
    return False


list1 = [3,1,2,5]
b = check(list1)
print(b)
'''
'''
def spy_game(nums):
    lis = []
    for i in nums:
        if i == 0 or i == 7:
            lis.append(i)

    for i in lis:
        if lis == [0, 0, 7]:
            print(True)
            break
        else:
            print(False)
            break

spy_game([1,2,4,0,0,7,5])
spy_game([1,7,2,0,4,5,0])
'''
'''
def findv(r):
    pi = 3.1415926535
    print(4/3 * pi * pow(r, 3))

findv(1)
findv(23)
'''
'''
def unique(l):
  x = []
  for i in l:
    if i not in x:
      x.append(i)
  return x

print(unique([1,2,3,3,3,3,4,5]))
'''
