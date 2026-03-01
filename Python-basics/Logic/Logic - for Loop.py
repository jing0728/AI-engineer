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