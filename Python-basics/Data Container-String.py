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

# s=' Hello-World-Hello-Python '
# #find()--在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1---> 样例：s.find("python")
# index = s.find("-")
# print(index)#6
# #count()--统计子串在字符串中出现的次数 ---> 样例：s.count("H")
# c = s.count('o')
# print(c)#4
# #upper()--将字符串中的所有字母转化为大写 --->样例：s.upper()
# print(s.upper())# HELLO-WORLD-HELLO-PYTHON 
# #lower()--将字符串中的所有字母转化为小写 --->样例： s.lower()
# print(s.lower())# hello-world-hello-python
# #split()--将字符串按指定分隔符分割成列表（list） ---> 样例: s.split("")
# slist=s.split("-")
# print(slist)#[' Hello', 'World', 'Hello', 'Python ']
# #strip()--去除字符串两端的空白字符串或者指定字符串 ---> 样例：s.strip()/s.strip('*')
# ss = s.strip()
# print(ss)#Hello-World-Hello-Python
# #replace()--将字符串中的指定字符串替换成新的子串 ---> 样例: s.replace('H','C')
# sr = s.replace("-","_")
# print(sr)#Hello_World_Hello_Python
# #startwith()--检查字符串是否以指定子串开头，返回布尔值 --->s.startwith('P')
# print(s.startswith('p'))#False
# print(s)#原始字符串不会变

# #案例：验证邮箱格式

# while True:
#     s = input("输入正确的邮箱地址：")
#     if (
#         s.count('@')==1 
#         and not s.startswith('@')
#         and '.' in s.split('@')[1]
#         and not s.endswith(".")
#         and not s.endswith("@")
#         #包含一个@，并且至少有一个.并且不已@开头          
#         ):
#             print('邮箱正确')
#             break

##正则表达式（Regular Expression）=用一种“规则语言”去匹配字符串模式--一个字符串长得像不像某种格式
#. -> 任意字符
# \d ->数字
# \w ->字母/数字/下划线
# + ->一个或者多个
# * ->零个或者多个
# ? ->零个或者一个
# ^ ->开头
# $ ->结尾

#案例：判断输入的是否为回文
#用户输入单词
# s = input("请输入任意单词来判断是否为回文：")
# # 前一半是否等于反过来的后一半
# # for i in range(len(s)//2):
# #     if s[i]==s[-(i+1)]:
# #         print(f"{s}是回文")#不要在for loop里面打印，不然每次对了都会打印是回文
# #     else:
# #         print(f"{s}不是回文")

# is_palindrome = True

#这个是分半来进行对比但是还不是最优解
# for i in range(len(s) // 2):
#     if s[i] != s[-(i + 1)]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print(f"{s}是回文")
# else:
#     print(f"{s}不是回文")

# #最优解
# if s == s[::-1]:#把字符串反转直接把字符串反转了，然后进行对比
#     print(f"{s}是回文")
# else:
#     print(f"{s}不是回文")
    

# #案例：输入十个字符，然后全部转为大写，记录在列表里，最后将列表的内容，遍历出来
# # l = []
# # for i in range(10):
# #     s=input(f"输入{10-i}个字符串: ")
# #     l.append(s.upper())
# # l.reverse()
# # print(l)
# #最优解
# l = [input(f"输入{10-_}个字符串: ").upper() for _ in range(10)]
# # l.reverse()
# # print(l)
# #这里还可以简化成
# print(l[::-1])

# #最终模板为
# l = [input(f"输入{10-_}个字符串: ").upper() for _ in range(10)]
# print(l[::-1])