###数据和逻辑
###条件判断--if语句：只有满足指定条件，才会执行对应的代码逻辑//python中通过缩进来描述代码的归属的，使用tab或者4个空格来进行缩进
#if语句的基本结构：
# if 要判断的条件:
#     满足条件时执行的代码逻辑
# else:
#     不满足条件时执行的代码逻辑

score = int(input("请输入你的高考成绩："))
if score >= 680:
    print("恭喜你，考上了清华大学！")
else:
    print("很遗憾，你没有考上清华大学。")

#案例：账号和密码验证
account = input("请输入正确的账号:")
password = input("请输入正确的密码：")
if password == "666888" and account == "1888888888":
    print("登入成功")
elif password != "666888" and account != "1888888888":
    print("账号和密码错误")
elif password != "666888":
    print("密码错误")
elif account != "1888888888":
    print("账号错误")

#案例：判断年份是否为闰年
years = int(input("请输入一个年份： "))
if (years % 4 ==0 and years %100 != 0) or (years % 400 ==0):
    print(f"{years}是闰年")
else:
    print(F"{years}不是闰年")

#案例：判断一个数是偶数还是奇数
number = int(input("Please enter a whole number: "))
if number % 2 == 0:
    print(f"{number} is an even number\n")
else:
    print(f"{number} is an odd nuymber\n")

#案例：判断年龄是否成年
age = int(input("Please enter your age: "))
if age >=18:
    print("You are an adult\n")
else:
    print("You are under age\n")

#案例：判断正负数
num = float(input("Please enter any number: "))
if num >0:
    print("{num} is a positive number\n")
elif num <0:
    print("{num} is a negative number\n")
else:
    print("{num} is zero\n")
#案例：判断考试成绩
grade = int(input("Enter your exam score: "))
if grade >= 60:
    print("Your are passed\n")  
else:    
    print("You are failed\n")  

#案例
user_name=str(input("请输入用户名: "))
passcode = str (input("请输入密码: "))
if (user_name == "admin" and passcode == "666888") or (user_name == "root" and passcode == "5475277") or (user_name == "zhangsan" and passcode == "123456"):
    print("登入成功")
else:
    print("用户名或密码错误")

#案例：根据成绩判断成绩等级
grade = int(input("enter your grade: "))
if grade >=85:
    print("Great")
elif 85>grade >=60:
    print("Good")
else:
    print("Fail")
#案例：折扣金额判断
amount = float(input("Enter your shopping amount: "))
if amount >= 500:
    print(f"The origanl amount is {amount}, you get the 20% off, the final amount is {amount*0.8}")
elif 300<=amount<500:
    print(f"The origanl amount is {amount}, you get the 10% off, the final amount is {amount*0.9}")
elif 100<=amount<300:
    print(f"The origanl amount is {amount}, you get the 5% off, the final amount is {amount*0.95}")
else:
    print("You did not get any discount")

#案例：判断三角形- pass 是一个空语句，起到一个语法占位的作用
side1 = float(input("请输入边长1： "))
side2 = float(input("请输入边长2： "))
side3 = float(input("请输入边长3： "))
if side1+side2>side3 and side1+side3 > side2 and side2+side3 > side1:#条件成立，形成三角形
    if side1 == side2 == side3:
        print("这是一个等边三角形")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("这是一个等腰三角形")
    else:
        print("这是一个普通三角形")
else:
    print("这不是一个三角形")

# #案例：电量
amount = float(input("请输入你本月用电量： "))
if amount<= 2880:
    print(f"你本月用电量为{amount},电费单价为0.4883，本月电费为{amount*0.4883}")
elif 2880<amount<=4800:
    print(f"你本月用电量为{amount},电费单价为0.5383，本月电费为{amount*0.5383}")
else:
    print(f"你本月用电量为{amount},电费单价为0.7883，本月电费为{amount*0.7883}")

###模式匹配:match...case--用一个清晰的模板去精确匹配数据的结构和内容，匹配成功则执行响应的操作
day = input("输入星期几")
match day:
    case "1":
        print("周一")
    case "2":
        print("周二")
    case "3":
        print("周三")
    case "4":
        print("周四")
    case "5":
        print("周五")
    case "6"| "7":#其中的 | 表示或/or的关系，匹配多个模式中的任意一个
        print("周末")
    case _:# _ 匹配其他所有的情况
        print("输入错误")

# 案例：输入数字和运算符进行运算
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
simple = input("输入你想进行的运算模式： ")
match simple:
    case "+":
        print(f"num1是{num1}，num2是{num2}，进行的运算是{simple}，结果是{num1+num2}")
    case "/":
        print(f"num1是{num1}，num2是{num2}，进行的运算是{simple}，结果是{num1/num2}")
    case "-":
        print(f"num1是{num1}，num2是{num2}，进行的运算是{simple}，结果是{num1-num2}")
    case "*":
        print(f"num1是{num1}，num2是{num2}，进行的运算是{simple}，结果是{num1*num2}")
    case _:
        print("没有办法进行运算哦")

#案例：游戏指令系统
move = input("请输入你的动作： ")
match move:
    case "上"|"w"|"W":
        print("角色向上移动")
    case "下"|"s"|"S":
        print("角色向下移动")
    case "左"|"a"|"A":
        print("角色向左移动")
    case "右"|"d"|"D":
        print("角色向右移动")
    case "跳"|" ":
        print("角色跳跃")
    case "攻击"|"j"|"J":
        print("角色发动攻击")
    case "推出"|"esc"|"ESC":
        print("角色退出游戏")
    case _:
        print("指令错误")

###循环

#while 循环：当满足指定条件时，重复执行对应的代码逻辑
#while循环的基本结构：
# while 条件:
#     满足条件时执行的代码逻辑
#     #更新条件的代码逻辑
# #案例：计算1到100的和
sum = 0
i =1
while i<=100:
    sum +=1
    i +=1
print(f"1到100的和是：{sum}")

#案例：打印5遍“Hello World”
i = 0
while i<5:
    print("Hello World")
    i +=1

#案例：1-100的偶数和
sum = 0
i = 0
while i <=100:
    sum += i
    i +=2  
print(f"1-100的偶数和是：{sum}")

sum = 0
i = 1
while i <=100:
    if i % 2 == 0:
        sum += i
    i +=1
print(f"1-100的偶数和是：{sum}")

#for循环：用于遍历一个序列（如列表、字符串等）中的元素，并对每个元素执行对应的代码逻辑
#for循环的基本结构：
# for 变量 in 序列:
#     对每个元素执行的代码逻辑
# #案例：打印列表中的每个元素
fruits = input("输入任何单词： ")
for i in fruits:
    print(f"元素：{i}")

#range()函数：生成一个整数序列，常用于for循环中指定循环的次数或范围
#range(end)：生成从0到end-1的整数序列---range(5)生成0,1,2,3,4
#range(start,end)：生成从start到end-1的整数序列---range(1,5)生成1,2,3,4
#range(start,end,step)：生成从start到end-1，步长为step的整数序列----range(1,10,2)生成1,3,5,7,9

#案例：计算1-100的奇数和
sum = 0
for i in range(0,101):
    if i % 2 == 1:
        sum += i
print(f"1-100的奇数和是：{sum}")

# 简化代码逻辑
sum = 0
for i in range(1,100,2): 
    sum += i
print(f"1-100的奇数和是：{sum}")

#案例：计算100-500之间所有3的倍数的数字之和
sum = 0
for i in range(100,501):
    if i%3 == 0:
        sum += i
print(f"100-500之间所有3的倍数的数字之和是：{sum}")

# 简化代码逻辑
sum = 0
for i in range(102,501,3):
    sum += i 
print(f"100-500之间所有3的倍数的数字之和是：{sum}")   

###嵌套循环：在一个循环内部又包含另一个循环，内层循环会在每次外层循环迭代时执行完整的循环过程
# 案例：打印长方形
length = int(input("请输入长方形的长度： "))
width = int(input("请输入长方形的宽度： ")) 
for i in range(length):
    for j in range(width):
        print("*",end="")#print语句自带换行功能，如果不想换行，可以使用end参数来指定结束符，例如end=""表示不换行，直接在同一行继续输出，end=
    print()

# 案例：打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="\t")
    print()

#案例：根据输入的边长打印对应的三角形
length=int(input("请输入三角形的边长: "))
for i in range(length+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#案例：根据输入的数字打印对应的数字金字塔
num=int(input("请输入数字: "))
for i in range(num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#案例：打印国际象棋棋盘
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            print("#",end=" ")
        else:
            print("*",end=" ")
    print()

#案例:用户登录验证
#关键字：
# break：用于退出循环
#continue：用于跳过当前循环的剩余代码，直接进入下一次循环的判断

while True:
    username=input("请输入你的用户名： ")
    password = input("请输入你的密码： ")
    if username =="" or password =="":
        print("不能为空，请重新输入")
        continue
    
    match (username,password):
        case ("admin","123456"):
            print("登录成功！")
            break#退出循环
        case ("zhangsan","666888"):
            print("登录成功！")
            break#退出循环
        case ("lisi","888666"):
            print("登录成功！")
            break#退出循环
        case _:
            print("用户名或密码错误，请重新输入。")


#案例：猜数字游戏
import random
num =random.randint(1,100)
while True:
    num_guess=int(input("请输入你猜的数字："))
    if num_guess not in range(1,100):
        print("你猜的数字不在范围内")
        continue
    if num_guess == num:
        print("猜对了")
        break
    elif num_guess>num:
        print("太大了")
    else:
        print("太小了")
    
# 案例：1-1000之间所有五的倍数的数字之和
sum=0
for i in range(0,1001,5):
    sum+=i
print(sum)

#案例：查询输入字符里面的a和k有几个
i=0
str = input("随意输入任意字符串： ")
for char in str:
    if char == 'a' or char == 'k':
        i+=1
print(i)