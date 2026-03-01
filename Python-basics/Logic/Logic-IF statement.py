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





 

