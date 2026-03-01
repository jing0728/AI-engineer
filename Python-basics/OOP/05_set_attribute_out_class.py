"""
案例：演示在类外 如何获取 和 设置 对象的属性
类外，设置对象的属性，格式如下：
    对象名.属性名=属性值
    特点：该属性独属于这个对象，即：该类的其他对象没有这个属性
类外，获取对象的属性，格式如下：
    对象名.属性名
"""

#需求：创建汽车类，设置为红色，有四个轮胎，有跑的功能
#1.创建汽车类
class Car:
    #属性(名词)
    # color = 'red'
    # tire = 4
    #行为（动词），事物能够做什么 -->函数
    def run(self):
        print("car can run")
#创建该类的对象
car1=Car()
car1.color = 'red'
car1.tire = 4
#打印car1对象的属性值
print(f"颜色是{car1.color},轮胎数量是{car1.tire}")
car1.run()

#继续创建该类的对象
car2=Car()
car2.color = 'blue'
car2.tire = 5
print(f"颜色是{car2.color},轮胎数量是{car2.tire}")
car2.run()