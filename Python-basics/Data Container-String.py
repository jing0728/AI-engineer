####字符串:字符的容器，一个字符串中可以存放任意的字符
#特点：不可变性（无法修改），有序性，可迭代性
#字符串中的每个字符都有其对应的下标(索引)

#可以切片，和列表切片一样
# s = 'Hello -World'
# print(s[4])
# print(s[-4])#字符串可以进行正向索引和反向索引
# # s[4]='b'
# # print(s[4])#TypeError: 'str' object does not support item assignment---字符串具有不可变性
# for i in s:
#     print(i)#字符串具有可迭代性

#切片
# print(s[0:6:1])
# print(s[0:6:])
# print(s[0:6])
# print(s[:6])#都是print out hello

# print(s[6:12:1])
# print(s[6:12:])
# print(s[6::])#print out -world

# print(s[::6])#步长为正，是从前往后
# print(s[::-6])#步长为负，是从后往前

s=' Hello-World-Hello-Python '
#find()--在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1---> 样例：s.find("python")
index = s.find("-")
print(index)#6
#count()--统计子串在字符串中出现的次数 ---> 样例：s.count("H")
c = s.count('o')
print(c)#4
#upper()--将字符串中的所有字母转化为大写 --->样例：s.upper()
print(s.upper())# HELLO-WORLD-HELLO-PYTHON 
#lower()--将字符串中的所有字母转化为小写 --->样例： s.lower()
print(s.lower())# hello-world-hello-python
#split()--将字符串按指定分隔符分割成列表（list） ---> 样例: s.split("")
slist=s.split("-")
print(slist)#[' Hello', 'World', 'Hello', 'Python ']
#strip()--去除字符串两端的空白字符串或者指定字符串 ---> 样例：s.strip()/s.strip('*')
ss = s.strip()
print(ss)#Hello-World-Hello-Python
#replace()--将字符串中的指定字符串替换成新的子串 ---> 样例: s.replace('H','C')
sr = s.replace("-","_")
print(sr)#Hello_World_Hello_Python
#startwith()--检查字符串是否以指定子串开头，返回布尔值 --->s.startwith('P')
print(s.startswith('p'))#False
print(s)