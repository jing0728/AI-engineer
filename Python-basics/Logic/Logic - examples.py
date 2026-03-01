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