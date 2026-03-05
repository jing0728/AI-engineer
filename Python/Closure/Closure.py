""" 
案例：闭包的背景介绍:保存外部函数的变量，延长外部函数的局部变量的生命周期

案例目的：
    引出来 闭包 相关的知识点 late binding
    
"""
#需求：定义函数保存变量10，调用函数返回值 并 重复累加数值，观察结果
#1.定义函数，保存变量10

def func(num):
    num=10
    def add(num2):
        nonlocal num
        for i in range(num2):
            num+=num2
        return num
    return add
add=func(2)
print(add(5))

""" 
案例：闭包的语法和用法介绍

闭包的定义
    在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数
    这种：使用 外部函数变量 的 内部函数 称为闭包

语法结构
    #外部函数
    def 外部函数名（外部参数）：
        外部函数的局部变量
        
        def 内部函数名（内部参数）：
            。。。使用外部函数的变量
        return 内部函数名    #闭包

闭包构成条件
    有嵌套              外部函数嵌套内部函数
    有引用              内部函数使用外部函数的变量
    返回内部函数         外部函数返回内部函数（对象不是return 值）
    
细节：
    函数名 和 函数名（）是两个概念，函数名表示 函数对象， 函数名（）表示调用函数，获取返回值
"""

#案例1：函数名-->是对象
def get_sum(a,b):
    return a+b
print(get_sum)  #是打印对象：<function get_sum at 0x000001D1CAD18220>
print(get_sum(2,4)) #是打印get_sum这个函数的返回值也就是：6


#案例2：演示闭包的写法
#需求：外部函数有参数num1，内部函数有参数num2，然后调用，并用于求解两数之和，
def func1(num1):
    def func2(num2):
        print(num2+num1)
    return func2

#调用函数
func2=func1(10)
func2(20)

func1(10)(20)

""" 
nolocal:
    python内置的关键字，能让内部函数修改外部函数的变量
"""
#需求：编写一个闭包，让内部函数可以访问外部函数的参数 a=100,并观察结果
def func(num):
    def func2(a):
        nonlocal num
        num=a
        print(num)
        return num
    return func2
func2=func(3)
print(func2(100))

#需求：写一个函数 outer()，让内部函数 inner() 可以访问外部变量 x。
def outer(x):
    def inner():
        return x
    return inner
f =outer(10)
print(f())

#需求：写一个闭包实现 计数器。
def outer(x):
    def inner():
        nonlocal x
        x=x+1
        return x
    return inner
c=outer(5)
print(c())
print(c())
print(c())

