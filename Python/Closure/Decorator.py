""" 
装饰器（decorator):
    不改变原有函数的基础上，给原有函数增加额外功能，装饰器本质上是一个闭包函数

装饰器的构成条件：
    有嵌套
    有引用
    有返回
    有额外功能
    
装饰器的用法：
    格式1：传统写法
        装饰后的函数名=装饰器名（被装饰的原函数名）
        装饰后的函数名（）
    格式2：语法糖
        在要被装饰的圆函数上，直接写@装饰器名，之后直接调用原有函数即可
        
"""
#定义函数，发表评论之前先登录
def login(func):
    def wrapper():
        print("请先登录")
        return func()  
    return wrapper

#定义函数，表示发表评论
@login
def comment():
    print("发表评论")

@login
def payment():
    print("充值中")   
#测试
c=comment
p=payment
c()
p()

""" 

"""