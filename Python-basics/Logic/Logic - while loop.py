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