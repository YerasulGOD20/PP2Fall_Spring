'''
import os
print(os.getcwd()) #Текущая директория
print(os.listdir())#все файлы и каталоги в pythonProject
path = str(input("Insert path : ")) #'C/Users/zulqa/pythonProject'
if os.path.exists(path): #проверка по директории
    print(True)
else:
    print(False)

print('Exist:', os.access('C\\Users\\Yerasyl\\6tsis\\Database.txt', os.F_OK))
print('Readable:', os.access('C\\Users\\Yerasyl\\6tsis\\Database.txt', os.R_OK))
print('Writable:', os.access('C\\Users\\Yerasyl\\6tsis\\Database.txt', os.W_OK))
print('Executable:', os.access('C\\Users\\Yerasyl\\6tsis\\Database.txt', os.X_OK))

with open('Database.txt') as f:
    print(sum(1 for _ in f))

file = open('Database.txt', 'a')
lis = str(input("Insert list : "))
lis1 = list(lis)
lis2 = str(lis1)
file.write(lis2)
file.close()
path1 = str(input("Path : "))
if os.path.exists(path1):
    os.removedirs('files')
else:
    print("Path doesn't exist ! ")'''
'''#1
import os
path=os.getcwd()
print("Files:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("Py and txt:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("all")
print([ name for name in os.listdir(path)])'''
'''#2
import os
a = input()
print(os.access(a, os.F_OK))'''
'''#3
import os
path = input()
print(os.path.exists(path))
path = input()
print(os.path.exists(path))
print("File name of the path:")
print(os.path.basename(path))
print("Dir name of the path:")
print(os.path.dirname(path))
print(os.getcwd())'''
'''#4
def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
print("Number of lines in the file: ", file_lengthy(input()))'''
'''#5
colour = input()
a = input()
with open(a, "w") as myfile:
        for c in color:
                myfile.write("%s" % c)

content = open(a)
print(content.read())'''
'''#6
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)'''
'''#7
with open(input()) as f:
    with open(input(), "w") as f1:
        for line in f:
            f1.write(line)'''
'''#8
import os
filePath = input()
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("Can not delete the file as it doesn't exists")'''
