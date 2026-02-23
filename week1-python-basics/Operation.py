#day2.py # is the comment line for the fast way to do comment is to use ctrl + / 
print("My name is Python")

####字面量：程序中直接书写的固定值
#整数（int）：表示没有小数部分的数字，例如1、-5、0等。
print(42)
#浮点数（float）：表示有小数部分的数字，例如3.14、-0.001等。
print(3.14)
#字符串（str）：表示文本数据，例如"Hello, World!"、'Python'等。
print("Hello, World!")
#布尔值（bool）：表示真（True）或假（False）的值。本质是数字类型，在涉及到数学运算时，会自动将True转换为1，False转换为0。
print(True)
print(False)
print(True + True)  # 输出2，因为True被转换为1
print(True + False) # 输出1，因为True被转换为1，False被转换为
#空值（None）：表示没有值或空值。
print(None)
#数据容量：储存多项数的容器，列表（list）、元组（tuple）、集合（set）和字典（dict）。

#变量：变量是一个命名的存储位置，用于保存数据值。变量可以存储不同类型的数据，并且可以在程序中被修改。
num = 1114.6
print(num)
num = num+1
print(num)
num = ("Hello, " + "world!")
print(num)
print(f"My name is {num}") #f-string allows you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and formatted using the __format__ protocol.

# 案例
view_count = 20.7
increase = 50
for i in range(2):
    i +=1
    print(f"基础播放量是{view_count},每月增加的播放量是{increase},第{i}个月总播放量是{view_count+i*increase}")

#变形
view_count,increase =20.7, 50
for i in range(2):
    i +=1
    print(f"基础播放量是{view_count},每月增加的播放量是{increase},第{i}个月总播放量是{view_count+i*increase}")

# 标识符
# 标识符是用来命名变量、函数、类等的名称。它必须遵循以下规则：
# 1.标识符只能包含字母、数字和下划线（_），并且必须以字母或下划线开头。
# 2.标识符不能是Python的保留字（如if、else、for、while等）。
# 3.标识符区分大小写，例如myVariable和myvariable是两个不同的标识符。
# 4.标识符不能以数字开头

# 规范
# 见名知意，变量名应具有描述性，便于理解其用途。例如，使用view_count而不是v，使用increase而不是inc。
# 多个部分使用下划线来区分
# 英文字母全部小写

#将a和b的值进行交换
a = 10 
b = 20
# c = a # c = 10
# a = b # a = 20
# b = c # b = 10
a,b = b,a #元组拆包，右边先求值，创建一个临时的元组(20,10)，然后将这个元组拆包赋值给a和b，最终实现了a和b的值交换。
print("a is ",a) # 输出20
print("b is ",b) # 输出10

#将a,b和c的值进行交换
a = 10
b = 20
c = 30

a, b, c = c, a, b # a = 30, b = 10, c = 20
print("a is ",a) # 输出30   
print("b is ",b) # 输出10
print("c is ",c) # 输出20   


#####常见的数据类型

#type()函数：用于查看变量的数据类型
print(type(10)) # 输出<class 'int'>
print(type(3.14)) # 输出<class 'float'>
print(type("Hello, World!")) # 输出<class 'str'>
print(type(True)) # 输出<class 'bool'>

#isinstance()函数：用于检查一个对象是否是某个特定类型的实例。如果是：True，否则返回False。
print(isinstance(10, int)) # 输出True
print(isinstance(3.14, float)) # 输出True   
print(isinstance("Hello, World!", int)) # 输出Flase

######字符串

#双引号定义
s1 = "Hello, World!"
#单引号定义
s2 = 'Hello, World!'
#三引号定义(多行字符串)
s3 = """Hello, World!
This is a multi-line string."""

print(s1)
print(s2)       
print(s3)

print(type(s1)) # 输出<class 'str'>
print(type(s2)) # 输出<class 'str'> 
print(type(s3)) # 输出<class 'str'>



# \' 单引号
# \" 双引号
# \\ 反斜杠
# \n 换行
# \t 制表符，增加一个缩进

msg ='\tIt\'s a nice day!\n \"Let\'s go outside.\"\\' #使用转义字符来处理字符串中的特殊字符，例如单引号和换行符。
print(msg)
#输出 
#It's a nice day!
# "Let's go outside."

####字符串的拼接
s1 = "Hello, "
s2 = "World!"
print(s1 + s2) # 输出Hello, World!

s3 = "hello" + " " + "world"#加号只能链接字符串，不能链接其他类型的数据，否则会报错。例如，"Hello, " + 42会导致TypeError，因为整数42不能直接与字符串连接。要解决这个问题，可以使用str()函数将非字符串类型转换为字符串，例如："Hello, " + str(42)将输出"Hello, 42"。
print(s3) # 输出hello world

s4 = "hello" " " "world"
print(s4) # 输出hello world

###字符串格式化
# %占位符 的形式完成字符串和变量的快速拼接。（其中% 表示我要占位， S表示我要占位的变量是字符串，d表示我要占位的变量是整数，f表示我要占位的变量是浮点数）
#案例-->str()函数：将其他类型的数据转换为字符串类型。
name = "Alice"
age = 30
pro = "engineer"
hobby = "painting"
print(f"My name is {name}, I am {age} years old, I work as an {pro}, and my hobby is {hobby}.") #f-string allows you to embed expressions inside string literals, using curly braces {}.
print("My name is " + name + ", I am " + str(age) + " years old, I work as an " + pro + ", and my hobby is " + hobby + ".") #使用str()函数将age转换为字符串，以便与其他字符串进行连接。
print("My name is %s, I am %d years old, I work as an %s, and my hobby is %s." % (name, age, pro, hobby)) #使用%占位符进行字符串格式化，%s表示字符串占位符，%d表示整数占位符，%f表示浮点数占位符。后面的括号中依次传入对应的变量。
print("My name is %s, I am %s years old, I work as an %s, and my hobby is %s." % (name, age, pro, hobby)) 

####输入与输出
# #input()函数：用于从用户输入获取数据。它会暂停程序的执行，等待用户输入，并将输入的数据作为字符串返回。
# #print()函数：用于将数据输出到控制台。它可以接受多个参数，并将它们转换为字符串后输出，默认以空格分隔。
name = input("请输入你的名字：") #提示用户输入名字，并将输入的值存储在变量name中。
age = input("请输入你的年龄：") #提示用户输入年龄，并将输入的值存储在变量age中。
print(f"你的名字是{name}，你的年龄是{age}岁。") #使用f-string格式化字符串，将用户输入的名字和年龄输出到控制台。
#无论输入的什么类型的数据，获取的数据类型永远都是字符串！！！

#案例
original_amount = 10000
password = input("请输入您的密码: ")
amount = input("请输入您要取的金额: ")
if int (amount) > original_amount:
    print("余额不足")
else:
    print(f"取款成功，您的余额是: {original_amount - int(amount)}")

#案例：输出两数之和
num1 = input("请输入第一个数字: ")
num2 = input("请输入第二个数字: ")
print(f"两个数字之和是：{int(num1)+int(num2)}")

###运算符
# 算术运算符：用于执行基本的数学运算，例如加法（+）、减法（-）、乘法（*）、除法（/）等。
# 比较运算符：用于比较两个值，并返回一个布尔值（True或False），例如等于（==）、不等于（!=）、大于（>）、小于（<）等。
# 逻辑运算符：用于组合多个条件，并返回一个布尔值，例如与（and）、或（or）、非（not）等。
# 赋值运算符：用于将一个值赋给一个变量，例如等于（=）、加等于（+=）、减等于（-=）等。

# #算术运算符
#+ 加法
print(10 + 5) # 输出15
#- 减法
print(10 - 5) # 输出5
#* 乘法
print(10 * 5) # 输出50
#/ 除法
print(10 / 5) # 输出2.0
#% 取模（返回除法的余数）
print(10 % 3) # 输出1，因为10除以3的商是3，余数是1
#// 整除（返回除法的整数部分）
print(10 // 3) # 输出3，因为10除以3的商是3.333...，整数部分是3
#** 幂运算（返回一个数的幂）
print(2 ** 3) # 输出8，因为2的3次幂是8

# 算术运算符的优先级：括号 > 幂运算 **> 乘法/除法/取模/整除 * / % //> 加法/减法 + -

#案例：计算两数之和与差
x = float(input("请输入数字x: "))
y = float(input("请输入数字y: "))
print(f"x + y = {x+y} ")
print(f"x - y = {x-y} ")# 0.1999999999999993  因为二进制浮点数表示的精度限制，导致了这个结果。计算机使用二进制来表示浮点数，而某些十进制的小数无法精确地转换为二进制，这就导致了精度损失，从而产生了这个近似值。

#案例1：计算三个数的平均值
print("请输入三个数字，我们将为您计算他们的平均值。")
num1 = float(input("第一个数字： "))
num2 = float(input("第二个数字： "))
num3 = float(input("第三个数字： "))
average = (num1 + num2 + num3) / 3
print(f"这三个数字的平均值是：{average}\n")

#案例二：要求输入梯形的上底、下底和高，计算梯形的面积并输出结果。
print("请输入梯形的上底、下底和高，我们将为您计算梯形的面积。")
top = float(input("上底： "))
bottom = float(input("下底： "))
height = float(input("高： "))
area = (top + bottom) * height / 2
print(f"梯形的面积是：{area}\n")

#案例三：输入圆的半径然后计算周长和面积
print("请输入圆的半径，我们将为您计算圆的周长和面积。")
r= float(input("圆的半径为："))
print(f"圆的周长是：{2*3.14*r}")
print(f"圆的面积是： {3.14*r**2}\n")

#案例四：BMI计算
print("请输入您的身高（米）和体重（公斤），我们将为您计算BMI。")
height = float(input("身高（米）： "))
weight = float(input("体重（公斤）： "))
bmi = weight / (height ** 2)
print(f"您的BMI是：{bmi}")

# # ###赋值运算符
# # = 赋值运算符：将右侧的值赋给左侧的变量。 num = 1+2
num = 1 + 2 # num的值是3
print(num) # 输出3
# # += 加等于运算符：将右侧的值加到左侧的变量上，并将结果赋给左侧的变量。 num += 1 # 等价于 num = num + 1
num += 1 # num的值是4
print(num) # 输出4
# # -= 减等于运算符：将右侧的值从左侧的 变量中减去，并将结果赋给左侧的变量。 num -= 1 # 等价于 num = num - 1
num -= 1 # num的值是3
print(num) # 输出3
# # *= 乘等于运算符：将左侧的变量乘以右侧的值，并将结果赋给左侧的变量。  num *= 2 # 等价于 num = num * 2
num *= 2 # num的值是6
print(num) # 输出6
# # /= 除等于运算符：将左侧的变量除以右侧的值，并将结果赋给左侧的变量。 num /= 2 # 等价于 num = num / 2
num /= 2 # num的值是3.0
print(num) # 输出3.0
# # %= 取模等于运算符：将左侧的变量取模右侧的值，并将结果赋给左侧的变量。num %= 3 # 等价于 num = num % 3
num1=10
num1%= 3 # num的值是1，因为10除以3的商是3，余数是1，所以num的值被更新为1。
print(num1) # 输出1
# # // = 整除等于运算符：将左侧的变量整除右侧的值，并将结果赋给左侧的变量。num //= 3 # 等价于 num = num // 3
num //= 3# num的值是0，因为10除以3的商是3.333...，整数部分是3，所以num的值被更新为3。
print(num1) 
# # **= 幂等于运算符：将左侧的变量提升到右侧的值的幂，并将结果赋给左侧的变量。 num **= 2 # 等价于 num = num ** 2
num **= 2 
print(num1)


####比较运算符
# # == 等于运算符：比较两个值是否相等，如果相等返回True，否则返回False。
print(10 == 10) # 输出True
print(10 == 5) # 输出False
# # != 不等于运算符：比较两个值是否不相等，如果不相等返回True，否则返回False。
print(10 != 5) # 输出True
print(10 != 10) # 输出False
# # > 大于运算符：比较左侧的值是否大于右侧
print(10 > 5) # 输出True
print(5 > 10) # 输出False
# # < 小于运算符：比较左侧的值是否小于右侧
print(5 < 10) # 输出True
print(10 < 5) # 输出False
# # >= 大于等于运算符：比较左侧的值是否大于或等于右侧
print(10 >= 5) # 输出True
print(10 >= 10) # 输出True
print(5 >= 10) # 输出False
# # <= 小于等于运算符：比较左侧的值是否小于或等于右侧
print(5 <= 10) # 输出True
print(10 <= 10) # 输出True
print(10 <= 5) # 输出False

####逻辑运算符
# # and 与运算符：当两个条件都为True时，返回True，否则返回False。
print(True and True) # 输出True
print(True and False) # 输出False
print(False and True) # 输出False
print(False and False) # 输出False
# # or 或运算符：当至少一个条件为True时，返回True，否则返回False。
print(True or True) # 输出True
print(True or False) # 输出True
print(False or True) # 输出True
print(False or False) # 输出False
# # not 非运算符：用于取反一个条件，如果条件为True，返回False；如果条件为False，返回True。
print(not True) # 输出False
print(not False) # 输出True
