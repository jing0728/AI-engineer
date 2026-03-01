"""
案例：演示类内如何获取对象的属性
回顾（总结）：
    1.类外访问类中的成员，可以通过 对象名. 的方式
    2.类内访问类中的成员，可以通过 self. 的方式
    3.类外通过 对象名.属性名 = 属性值 的方式 设置属性， 只要当前对象有

细节：
    类内如何设置属性，要结合 魔法方法 __init__ () 来实现
"""
#1.定义汽车类，创建该类对象，赋予颜色 和 轮胎数两个属性，并在类内访问该属性
class Car:
    #属性

    #行为-跑
    def run(self):
        print("car can run")
    #定义函数show()，实现 在类内访问 汽车对象的属性
    def show(self):
        print(f'我是show函数，对象的颜色：{self.color},轮胎数是{self.number}')
#2.创建汽车类的对象
c1 = Car()

#3.给c1赋予 属性 --> 类外设置属性
c1.color = 'red'
c1.number = 4

#4.类外访问属性.
print(f"颜色：{c1.color},轮胎数量{c1.number}")

#5.类外访问行为
c1.run()
c1.show()

print("-"*54)
#6.继续创建c2汽车类
c2 = Car()
c2.color = 'blue'
c2.number = 4
print(f"颜色：{c2.color},轮胎数量{c2.number}")
c2.run()
c2.show()