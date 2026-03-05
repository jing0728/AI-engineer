# # """ 
# # 装饰器（decorator):
# #     不改变原有函数的基础上，给原有函数增加额外功能，装饰器本质上是一个闭包函数

# # 装饰器的构成条件：
# #     有嵌套
# #     有引用
# #     有返回
# #     有额外功能
    
# # 装饰器的用法：
# #     格式1：传统写法
# #         装饰后的函数名=装饰器名（被装饰的原函数名）
# #         装饰后的函数名（）
# #     格式2：语法糖
# #         在要被装饰的圆函数上，直接写@装饰器名，之后直接调用原有函数即可
        
# # """
# # #定义函数，发表评论之前先登录
# # def login(func):
# #     def wrapper():
# #         print("请先登录")
# #         func()  
# #     return wrapper

# # #定义函数，表示发表评论
# # @login
# # def comment():
# #     print("发表评论")

# # @login
# # def payment():
# #     print("充值中")   
# # #测试
# # c=comment
# # p=payment
# # c()
# # p()

# """ 
# 案例：装饰器装饰_无参无返回的原函数

# 细节：
#     装饰器的内部函数结构 要和原函数的格式一样
#     例如：原函数是无参无返回的，那装饰器也要是无参无返回的
# """

# #案例：定义无参无返回值的get_sum()求和函数，在不改变其代码的基础上，添加友好提示：
# def notice(func):
#     def fn_inner():
#         print("正在努力计算中...")
#         func()
#     return fn_inner

# @notice
# def get_sum():
#     a=10
#     b=5
#     print(a+b)

# get_sum()


# #案例：定义有参无返回值的get_sum()求和函数，在不改变其代码的基础上，添加友好提示：
# def notice(func):
#     def fn_inner(*args,**kwargs): #*args-接收所有“位置参数”-->并且会被打包成一个 tuple（元组）  #**kwargs -接收所有“关键字参数”-->并且会被打包成 dict（字典）
#         print("正在努力计算中...")
#         func(*args,**kwargs)
#     return fn_inner

# @notice
# def get_sum(a,b):
#     print(a+b)

# get_sum(5,6)

# #案例：定义有参有返回值的get_sum()求和函数，在不改变其代码的基础上，添加友好提示：
# def notice(func):
#     def fn_inner(*args,**kwargs): #*args-接收所有“位置参数”-->并且会被打包成一个 tuple（元组）  #**kwargs -接收所有“关键字参数”-->并且会被打包成 dict（字典）
#         print("正在努力计算中...")
#         return func(*args,**kwargs)
#     return fn_inner

# @notice
# def get_sum(a,b):
#     sum=print(a+b)
#     return sum

# get_sum(5,6)

# #案例：定义无参有返回值的get_sum()求和函数，在不改变其代码的基础上，添加友好提示：
# def notice(func):
#     def fn_inner(): #*args-接收所有“位置参数”-->并且会被打包成一个 tuple（元组）  #**kwargs -接收所有“关键字参数”-->并且会被打包成 dict（字典）
#         print("正在努力计算中...")
#         return func()
#     return fn_inner

# @notice
# def get_sum():
#     a=10
#     b=5
#     sum=print(a+b)
#     return sum

# get_sum()

# #案例：定义可变参数的get_sum()求和函数，在不改变其代码的基础上，添加友好提示：
# def notice(func):
#     def fn_inner(*args,**kwargs): #*args-接收所有“位置参数”-->并且会被打包成一个 tuple（元组）  #**kwargs -接收所有“关键字参数”-->并且会被打包成 dict（字典）
#         print("正在努力计算中...")
#         return func(*args,**kwargs)
#     return fn_inner

# @notice
# def get_sum(*args,**kwargs):
#     # sum=0
#     # for i in args:
#     #     sum+=i
#     # for key in kwargs.values():
#     #     sum+=key
#     return sum(args)+sum(kwargs.values())

# sum=get_sum(1,2,3,4,a=2,b=9,v=8)
# print(sum)


# """ 
# 案例：多个装饰器装饰一个函数
# 记忆：
#     多个装饰器装饰一个函数，是按照 由内向外的顺序来装饰的
#     但是如果你要是用 装饰器的写法来做，看到的效果是：从上到下执行的
# """
# #需求：发表评论前，先登入验证，再验证码验证
# def login(func):
#     def fn_inner():
#         print("登入验证：")
#         func()
#     return fn_inner
# def code(func):
#     def fn_inner():
#         print("验证码验证：")
#         func()
#     return fn_inner

# @login
# @code
# def comment():
#     print("发表评论")
# comment()

# #传统写法
# comment=login(code(comment))
# comment()


""" 
一个装饰器有并且只能有一个参数
带有参数的装饰器，其实是再装饰器 外面又包裹 了一个函数，使用该函数接收参数， 返回装饰器

"""

#定义一个既能装饰减法又能装饰加法的装饰器
def func(flag):
    def func(fun):
        def fn_inner(*args,**kwargs):
            if flag =='+':
                print(f"现在在运算的是{flag}法")
                fun(*args,**kwargs)
            if flag =='-':
                print(f"现在在运算的是{flag}法")
                fun(*args,**kwargs)
            
        return fn_inner
    return func
@func('+')
def add(a,b):
    print(a+b)
    
@func('-')
def sub(a,b):
    print(a-b)
    
add(4,5)
sub(5,4)