    #抽象类（Abstract Class）--抽象类（Abstract Class）-->半成品父类
    #抽象方法（Abstract method）--
"""
案例：演示抽象类的用法。

抽象类解释：

概述：
    在Python中，抽象类 = 接口，即：有抽象方法的类就是 抽象类，也叫 接口。
    抽象方法 = 没有方法体的方法，即：方法体是 pass 修饰的。

作用 / 目的：
    抽象类一般充当父类，用于指定行业规范、准则，具体的实现交由 子类 来完成。
"""

#1.定义抽象类：空调类，设定：空调类的规则
class AC():
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_wind(self):
        pass
#2.定义子类
class Xiaomi(AC):
    def cool_wind(self):
        print("Xiaomi技术cool_wind")
    def hot_wind(self):
        print("Xiaomi技术hot_wind")
    def swing_wind(self):
        print("Xiaomi技术swing_wind")
class Huwei(AC):
    def cool_wind(self):
        print("Huwei技术cool_wind")
    def hot_wind(self):
        print("Huwei技术hot_wind")
    def swing_wind(self):
        print("Huwei技术swing_wind")

#3.测试
if __name__ == "__main__":
    xm = Xiaomi()
    xm.cool_wind()
    xm.hot_wind()
    xm.swing_wind()
    
    hw=Huwei()
    hw.cool_wind()
    hw.hot_wind()
    hw.swing_wind()
    