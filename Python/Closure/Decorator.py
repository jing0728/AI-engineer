# """ 
# 装饰器（decorator):
#     不改变原有函数的基础上，给原有函数增加额外功能，装饰器本质上是一个闭包函数

# 装饰器的构成条件：
#     有嵌套
#     有引用
#     有返回
#     有额外功能
    
# 装饰器的用法：
#     格式1：传统写法
#         装饰后的函数名=装饰器名（被装饰的原函数名）
#         装饰后的函数名（）
#     格式2：语法糖
#         在要被装饰的圆函数上，直接写@装饰器名，之后直接调用原有函数即可
        
# """
# #定义函数，发表评论之前先登录
# def login(func):
#     def wrapper():
#         print("请先登录")
#         func()  
#     return wrapper

# #定义函数，表示发表评论
# @login
# def comment():
#     print("发表评论")

# @login
# def payment():
#     print("充值中")   
# #测试
# c=comment
# p=payment
# c()
# p()

""" 
案例：装饰器装饰_无参无返回的原函数

细节：
    装饰器的内部函数结构 要和原函数的格式一样
    例如：原函数是无参无返回的，那装饰器也要是无参无返回的
"""

#案例：定义无参无返回值的get_sum()求和函数，在不改变其代码的基础上，添加友好提示：
def notice(func):
    def fn_inner():
        print("正在努力计算中...")
        func()
    return fn_inner

@notice
def get_sum():
    a=10
    b=5
    print(a+b)

get_sum()


#案例：定义有参无返回值的get_sum()求和函数，在不改变其代码的基础上，添加友好提示：
def notice(func):
    def fn_inner(*args,**kwargs): #*args-接收所有“位置参数”-->并且会被打包成一个 tuple（元组）  #**kwargs -接收所有“关键字参数”-->并且会被打包成 dict（字典）
        print("正在努力计算中...")
        func(*args,**kwargs)
    return fn_inner

@notice
def get_sum(a,b):
    print(a+b)

get_sum(5,6)