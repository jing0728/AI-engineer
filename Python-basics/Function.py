####函数--是组织好的，可重复是要的，用来实现特定功能的代码片段
####函数基础
#函数是组织好的，可重复使用的，用来实现特定功能的代码片段
#函数的定义与调用
#定义函数
"""def 函数名（参数列表）：
    函数体
    .....
    return 返回值
"""
#调用函数
"""
函数名(参数)
"""
# def out_line():
#     print("______________________")
#     print("______________________")
# out_line()

#案例：计算圆形的面积
# def area_circle(r):
#     area = 3.14*r**2
#     return area
# print(area_circle(2))

# #案例：计算长方形的面积
# def area_rectangle(a,b):
#     area=a*b
#     return area
# print(area_rectangle(7,8))

# # 案例：计算圆形的面积--->如果返回值有多个--->多个返回值会封装到元组当中
# def area_circle(r):
#     area = 3.14*r**2
#     length = round(3.14*2*r,1)#round()保留小数点
#     return area,length
# area,len=area_circle(5)
# print(area)
# print(len)

#help()--->用于查看函数的的说明文档
####函数的说明文档：用三引号包裹的字符串，用于解释函数的功能，参数，返回值等信息，方便调用者清楚函数的具体作用及细节
# # 案例：计算圆形的面积
# def area_circle(r):
#     """
#     该函数用于根据圆的半径，计算圆的面积和圆的周长
#     :param r :圆的半径 # :param -->描述函数的参数
#     :return：圆形的面积和周长 #:return --->-->描述函数的返回值
#     """
#     area = 3.14*r**2
#     return area
# print(area_circle(2))

# ####函数的嵌套调用：嵌套调用指的是在一个函数中，又调用了另一个函数
# #函数调用遵循栈结构，最后被调用的函数最先返回LIFO(Last In First Out, 后进先出)

# # 函数的嵌套调用

# def function_a():  # 1 个用法
#     print("a ... before")
#     function_b()
#     print("a ... after")

# def function_b():  # 1 个用法
#     print("b ... before")
#     function_c()
#     print("b ... after")

# def function_c():  # 1 个用法
#     print("c ...")

# function_a()

# print("函数调用完毕 ~")

#案例:
#定义一个函数：根据传入的底和高计算三角形面积的函数三角形面积 = 底 * 高 / 2）。
# def area(b,h):
#     """
#     该函数用于根据三角形底和高来进行计算三角形的面积
#     :param b: 三角形的底
#     :param b: 三角形的高
#     :return: 三角形的面积
#     """
#     return h*b/2

#定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
# def vowel(s):
#     """
#     该函数根据用户输入的字符串来排定字符串中的元音个数
#     :param s: 用户输入的字符串
#     :return: 元音的个数
#     """
#     num = 0
#     for ch in s:
#         if ch in "aeiouAEIOU":
#             num += 1
#     return num
# def vowel(s):
#     return sum(ch in "aeiouAEIOU" for ch in s)
# s = input("请输入一串英文：")
# count = vowel(s)
# print(f"一共有 {count} 个元音字母")

#定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数），并返回。
# def score(s):
#     return round(max(s),1),round(min(s),1),round(sum(s)/len(s),1)
# s = int(input("请输入高考成绩"))
# max_score,min_score,avg_score=score(s)
# print(f"最高分是{max_score}，最低分是{min_score}，平均分是{avg_score}")

####函数进阶

##函数变量的作用域：变量的作用范围
# #全局变量：在函数之外定义的变量，在整个文件中都可以使用
# #局部变量：只可以在函数内部使用
# num =100
# def area_circle(r):
#     pi=3.14
#     area = pi*r**2
#     global num  #global用于明确的告诉python，在函数中要使用全局变量，使得可以在函数内部修改全局变量的值
#     num=1000
#     print("num",num)
#     length = round(3.14*2*r,1)#round()保留小数点
#     return area,length
# print(area_circle(10))
# print("num",num)

#函数参数的详解
#传参方式
#位置参数：调用函数是根据函数定义时候的位置来传递参数。调用函数时参数顺序与定义函数时参数顺序完全一致
#关键字参数：调用函数时以函数定义时形参名称作为关键字，以“键”=“值”的形式来传递参数（顺序不要求一样）
#关键字参数永远在位置参数之后

# def reg_stu(name, age, gender, city):
#     print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
# stu=reg_stu("江南",24,"Male","NY")
# print(stu)
# stu1=reg_stu(name="江北",age=24,gender="Female",city="NJ")
# stu2=reg_stu(age=24,gender="Female",name="江北",city="NJ")
# print(stu1)
# stu3=reg_stu("江西",24,city="NK",gender="None")
# print(stu3)

#默认参数也称为缺省参数，用于在定义函数时，为函数提供默认值，调用函数时，可以部传递有默认值的参数,默认参数要在非默认参数后面
# def reg_stu(name, age, gender="M", city="GA"):
#     print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
# stu=reg_stu("Mike",24)
# print(stu)
# stu=reg_stu("Jane",25,"F")
# print(stu)

# #不定长参数（可变参数），用于函数定义以及调用时参数个数不确定的场景---位置传递，关键字传递
# #位置传递（*args)-将数据封装到元组里面
# #关键字传递（**kwagrs)-将数据封装到字典（dict）里面
# def calc_data(*args,**kwargs):
#     """
#     :param args:不定长位置参数，需要计算的这批数据
#     :param kwargs：不定长关键字参数
#         round：保留的小数位
#         print:是否打印输出
#     :return:
#     """
#     return min(args),max(args),round(sum(args)/len(args),kwargs.get("round"))
# data=calc_data(10,20,20,3,0,5,7,9,45)
# print(data)

#参数类型
#特殊参数：函数
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def calc(x,y,oper):
    return oper(x,y)
print(calc(7,8,add))