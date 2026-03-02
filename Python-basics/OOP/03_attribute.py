# """
# 案例：演示在类外 如何获取 和 设置 对象的属性
# 类外，设置对象的属性，格式如下：
#     对象名.属性名=属性值
#     特点：该属性独属于这个对象，即：该类的其他对象没有这个属性
# 类外，获取对象的属性，格式如下：
#     对象名.属性名
# """

# #需求：创建汽车类，设置为红色，有四个轮胎，有跑的功能
# #1.创建汽车类
# class Car:
#     #属性(名词)
#     # color = 'red'
#     # tire = 4
#     #行为（动词），事物能够做什么 -->函数
#     def run(self):
#         print("car can run")
# #创建该类的对象
# car1=Car()
# car1.color = 'red'
# car1.tire = 4
# #打印car1对象的属性值
# print(f"颜色是{car1.color},轮胎数量是{car1.tire}")
# car1.run()

# #继续创建该类的对象
# car2=Car()
# car2.color = 'blue'
# car2.tire = 5
# print(f"颜色是{car2.color},轮胎数量是{car2.tire}")
# car2.run()

# """
# 案例：演示类内如何获取对象的属性
# 回顾（总结）：
#     1.类外访问类中的成员，可以通过 对象名. 的方式
#     2.类内访问类中的成员，可以通过 self. 的方式
#     3.类外通过 对象名.属性名 = 属性值 的方式 设置属性， 只要当前对象有

# 细节：
#     类内如何设置属性，要结合 魔法方法 __init__ () 来实现
# """
# #1.定义汽车类，创建该类对象，赋予颜色 和 轮胎数两个属性，并在类内访问该属性
# class Car:
#     #属性

#     #行为-跑
#     def run(self):
#         print("car can run")
#     #定义函数show()，实现 在类内访问 汽车对象的属性
#     def show(self):
#         print(f'我是show函数，对象的颜色：{self.color},轮胎数是{self.number}')
# #2.创建汽车类的对象
# c1 = Car()

# #3.给c1赋予 属性 --> 类外设置属性
# c1.color = 'red'
# c1.number = 4

# #4.类外访问属性.
# print(f"颜色：{c1.color},轮胎数量{c1.number}")

# #5.类外访问行为
# c1.run()
# c1.show()

# print("-"*54)
# #6.继续创建c2汽车类
# c2 = Car()
# c2.color = 'blue'
# c2.number = 4
# print(f"颜色：{c2.color},轮胎数量{c2.number}")
# c2.run()
# c2.show()

"""案例：演示对象属性 和 类属性。

属性介绍：

概述：
    它是1个名词，用来描述事物的外在特征的。

分类：
    对象属性：属于每个对象的，即：每个对象的属性值可能都不同。修改A对象的属性，不影响对象B
    类属性：属于类的，即：能被该类下所有的对象所共享。A对象修改类属性，B对象访问的是修改后的。

对象属性：
    定义到 __init__ 魔法方法中的属性，每个对象都有自己的内容。
    只能通过 对象名. 的方式调用。

类属性：
    定义到类中，函数外的属性（变量），能被该类下所有的对象所共享。
    既能通过 类名. 还能通过 对象名. 的方式调用，推荐使用 类名. 的方式。
"""

#需求：演示 对象属性 和 类属性相关
#1.定义 1 个student类，每个学生都有自己的 姓名，年龄
class Student:
    #定义对象属性，即：写到 init魔法方法中的属性
    teacher_name='水镜先生'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #定义str魔法方法，输出对象的信息
    def __str__(self):
        return f"姓名{self.name},年龄{self.age}"
    
#5.测试
if __name__ == "__main__":
    s1=Student("jing",34)
    
    s2=Student("nan",77)
    # 场景2：类属性
    # 1. 类属性可以通过 类名，还可以通过 对象名 的方式调用。
    print(s1.teacher_name)        # 水镜先生
    print(s2.teacher_name)        # 水镜先生
    print(Student.teacher_name)   # 水镜先生
    print('-' * 23)

    # 2. 尝试用 对象名 的方式来修改 类属性
    # s1.teacher_name = '秀哥'   # 只能给s1对象赋值，不能给类属性赋值。

    # 3. 如果要修改类属性的值，只能通过 类名 的方式实现。
    Student.teacher_name = '秀哥'
    print(s1.teacher_name)        # 秀哥
    print(s2.teacher_name)        # 秀哥
    print(Student.teacher_name)   # 秀哥