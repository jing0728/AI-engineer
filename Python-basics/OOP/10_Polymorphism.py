####多态：同一个函数在不同的场景下有不同的状态
"""
实现多态的三个条件

有继承
（定义父类、定义子类，子类继承父类）

函数重写
（子类重写父类的函数）

父类引用指向子类对象
（子类对象传给父类对象调用者）
"""

"""
案例：演示多态入门。

多态概述：

专业版：同一个函数，接收不同的参数，有不同的效果  
大白话：同一个事物在不同时刻表现出来的不同状态、形态。

前提条件：
    1. 要有继承。
    2. 要有方法重写，不然多态无意义。
    3. 要有父类引用指向子类对象。
"""
# #1.定义动物类
# class Animal:    #抽象类（也叫：接口）
#     def speak(self): #抽象方法
#         print("动物会叫")
# # 2. 定义子类，狗类。
# class Dog(Animal):
#     def speak(self):
#         print('狗叫：汪汪汪')


# # 3. 定义子类，猫类。
# class Cat(Animal):
#     def speak(self):
#         print('猫叫：喵喵喵')

# #汽车类
# class Car:
#     def speak(self):
#         print('汽车叫：嘟嘟嘟')

# # 4. 定义函数，接收不同的动物对象，执行 speak 方法。
# def make_noise(an:Animal): #
#     an.speak()
# #5.测试
# if __name__ == "__main__":
#     # an:Animal = Dog()       #父类引用指向子类对象
#     # d:Dog=Dog()     #创建狗类对象
#     #5.1创建狗类，猫类对象
#     d = Dog()
#     c = Cat()
#     #5.2演示多态
#     make_noise(d)
#     make_noise(c)
#     #5.3 测试汽车类
#     ca = Car()
#     make_noise(ca)

"""
案例：演示Python的多态案例之 战斗平台。

需求：

    1. 构建对战平台（公共的函数）object_play()，接收：英雄机 和 敌机。
    2. 在不修改对战平台代码的情况下，完成多次战斗。
    3. 规则：
        英雄机，1代战斗力为60，2代战斗力80
        敌机，1代战斗力70

代码提示：

    英雄机1代 HeroFighter
    英雄机2代 AdvHeroFighter
    敌机 EnemyFighter
"""
#1.定义英雄机一代，战斗力六十
class HeroFighter():
    def power(self):
        return 60

#2.定义英雄机二代，战斗力八十
class HeroFighter2(HeroFighter):
    def power(self):
        return 80

#3.定义敌机，战斗力七十
class EnmeyFighter():
    def power(self):
        return 70
    
#4.构建对战平台，公共的函数，接受不同的参数，有不同的效果
def fight(hero:HeroFighter,enmey:EnmeyFighter):
    if hero.power()>enmey.power():
        print("英雄机 战胜 敌机")
    else:
        print("英雄机 惜败 敌机")
        
#5.测试
if __name__ == "__main__":
    #思路一不使用多态
    #场景一：英雄机一代 vs 敌机
    h1 = HeroFighter()
    e1 = EnmeyFighter()
    if h1.power() >= e1.power():
        print("英雄机一代 战胜 敌机")
    else:
        print("英雄机一代 惜败 敌机")
    #使用多态
    fight(h1,e1)
    #场景二：英雄机二代 vs 敌机
    h2 = HeroFighter2()
    e1 = EnmeyFighter()
    if h2.power()>= e1.power():
        print("英雄机二代 战胜 敌机")
    else:
        print("英雄机二代 惜败 敌机")
     #使用多态
    fight(h2,e1)
    
    #fight(h2,h1) #Python 是Duck Typing so有没有(hero:HeroFighter,enmey:EnmeyFighter)都会正常运行，只是会报警告而已