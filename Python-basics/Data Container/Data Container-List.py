####数据容器：一种数据结构，能够存储多个数据的对象。常见的数据容器有：列表、元组、集合、字典等。
# 列表（list）：一种有序、可变的容器，可以存储任意类型的数据。
# 字符串（str）：一种有序、不可变的容器，用于存储文本数据。
# 元组(tuple)：一种有序、不可变的容器，可以存储任意类型的数据。
# 集合(set)：一种无序、可变的容器，可以存储任意类型的数据，但不允许重复。
# 字典(dict)：一种无序、可变的容器，可以存储键值对数据，键必须是唯一的。

####列表（list)
# 列表的定义：使用方括号[]来定义一个列表，元素之间用逗号分隔。
# 列表的访问：使用索引来访问列表中的元素，索引从0开始。可以反向访问列表中的元素，使用负数索引，-1表示最后一个元素，-2表示倒数第二个元素，以此类推。
# 列表的修改：列表是可变的，可以通过索引来修改列表中的元素。
# 列表的添加：使用append()方法在列表末尾添加元素，使用insert()方法在指定位置添加元素。
# 列表的删除：使用del语句删除指定位置的元素，使用remove()方法删除指定值的元素，使用pop()方法删除指定位置的元素并返回该元素。
# 列表的切片：使用切片操作来获取列表的子列表，切片的语法为：list[start:stop:step]，其中start表示起始索引，stop表示结束索引（不包含），step表示步长。

# 列表的常用方法：
# append()方法在列表末尾添加元素
# insert()方法在指定位置添加元素
# remove()方法删除指定值的元素
# pop()方法删除指定位置的元素并返回该元素
# len()函数获取列表的长度
# count()方法统计列表中某个元素的出现次数
# index()方法获取列表中某个元素的索引
# sort()方法对列表进行排序
# reverse()方法反转列表等
# del()语句删除指定位置的元素
# 切片的语法为：list[start:stop:step]，其中start表示起始索引，stop表示结束索引（不包含），step表示步长

#列表的定义
s = [50,20,50,10,'Hello World',True,3.14]
# #列表的类型
# print(type(s))



# 切片的语法为：list[start:stop:step]，其中start表示起始索引，stop表示结束索引（不包含），step表示步长
# #获取列表的子列表
print(s[1:4]) #获取索引1到3的元素，索引4的元素不包含在内
print(s[::2]) #获取列表中所有偶数索引的元素
print(s[::-1]) #获取列表中所有元素的反向顺序,也是就reverse()方法的功能

# 遍历列表中的元素
for i in s:
    print(i)

####列表切片：切片是指对操作的数据截取其中的一部分的操作。
s = ["a","b","c","d","e","f"]
# # 切片的语法为：list[start:stop:step]，其中start表示起始索引，stop表示结束索引（不包含），step表示步长
print(s[0:5:2])# ['a', 'c', 'e']
print(s[0:5])# ['a', 'b', 'c', 'd', 'e']
print(s[:5])# ['a', 'b', 'c', 'd', 'e']
print(s[5])# f
print(s[:-2]) # ['a', 'b', 'c', 'd']

###列表的方法

print(s[0]) #访问第一个元素
print(s[-1]) #访问最后一个元素

# append()方法在列表末尾添加元素
s.append('Python')
print(s)

# insert()方法在指定位置添加元素
s.insert(3,"pig")
print(s)

# remove()方法删除指定值的元素，匹配到的第一个值
s.remove(50)
print(s)

# del()语句删除指定位置的元素
del s[2]
print(s)

# pop()方法删除指定位置的元素并返回该元素，（如果未指定索引，默认删除最后一个）
s.pop(2)
print(s)

# sort()方法对列表进行排序
s.sort() #列表中元素类型不一致，无法排序，会报错
print(s)

# reverse()方法 反转列表
s.reverse()
print(s)

#s[3] = "pig" #直接通过索引修改列表中的元素
s[3] = "pig"
print(s)

# set()方法对列表进行去重处理
s.set()
print(s)

# len()函数获取列表的长度
print(len(s))

# count()方法统计列表中某个元素的出现次数
print(s.count(50))

# index()方法获取列表中某个元素的索引
print(s.index(10))

#案例-用户输入数字然后进行排序，求平均值，最大值和最小值
s = []
for i in range(10):
    s.append(int(input("请输入十个数字：")))
print(s)
print(sum(s))
print(sum(s)/len(s))
s.sort()
print(s)
print(min(s)) 
print(max(s))

num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
# num_list3 = sorted(set(num_list1+num_list2)) - set 方法
num_list3 = sorted(num_list2+num_list1)
num_list3=[*num_list1,*num_list2]
s = []
for i in num_list3:
    # if  (not s) or (s[-1] !=i):#当列表不为空，并且最后一位不和之前的相同
    #     s.append(i)#则向列表中加入i
    if i not in s:
        s.append(i)
print(s)


#解包：将列表这一类容器解开成一个一个独立的元素

#基本写法
a, *b = [1, 2, 3, 4]#*变量 会接收“剩余所有元素”
print(a)  # 1
print(b)  # [2, 3, 4]
#组包：将多个值合并到一个容器

a, *b, c = [1, 2, 3, 4, 5]#也可以放中间，只能有一个 *
# a = 1
# b = [2, 3, 4]
# c = 5

# 单星号：拆位置参数
def add(a, b, c):
    print(a + b + c)

nums = [1, 2, 3]
add(*nums)# 等于add(1, 2, 3)

#双星号：拆字典参数
def show(name, age):
    print(name, age)

info = {"name": "Tom", "age": 20}
show(**info)#等于show(name="Tom", age=20)

#列表/字典合并解包
a = [1, 2]
b = [3, 4]

c = [*a, *b]
print(c)#[1, 2, 3, 4]

#案例：生成1-20的平方列表
s=[]
for i in range(1,21):
    a = i**2
    s.append(a)
print(s)

#方式2：列表推导式：按照一定的规则，快速生成列表--->语法格式：[要插入的值 for i in 序列/列表]
n = [i**2 for i in range(1,21)]
print(n)

#案例：从下列数字列表中提取偶数，并且进行平方
s = [19,23,54,64,87,20,109,232,123,43,26,55,72]
n = []
for i in s:
    if i%2==0:
        n.append(i**2)
print(n)

# #方式2：--->语法格式： [要插入的值 for i in 序列/列表 if/条件]
n = [(i**2) for i in s if i%2==0]
print(n)

#案例1：去重+相加+排序
L1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
L2 = ['X','Z','T','Y','D','E','F','G']
L3 = ['W','A','S','D']
print(sorted(set(L1+L2+L3)))

#案例2：三五整除元素提取加平方
n = [i**2 for i in range(1,31) if i%3==0 or i%5==0]
print(n)

#案例3：将列表里面的正数提取出来，封装成一个新列表
L1 = [11,2,31,4,-5,15,17,28,49,18,10,-11,16,54,-14,36,-16,87,-39]
L2 = [i for i in L1 if i>=0]
print(L2)



