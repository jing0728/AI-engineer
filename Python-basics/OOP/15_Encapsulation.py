"""
私有属性和私有方法

在 Python 中，可以为属性和方法设置私有权限，即设置某个属性或方法不继承给子类。
设置私有属性和方法的方式：在属性或方法名前面加上 __，格式：
# 私有属性
__属性名

# 私有方法
def __方法名():
    ...

私有属性和方法使用规则：
    只能在类的内部使用，不能在类的外部使用；
    
    如果想在类的外部使用，通过公共接口。
"""

"""
案例：演示封装之私有属性。

封装简介：

概述：
    属于面向对象的三大特征之一，就是隐藏对象的属性和实现细节，
    仅对外提供公共的访问方式。

怎么封装？
    我们学的 函数、类 都是封装的体现。

好处：
    1. 提高代码的安全性。      由 私有化 来保证
    2. 提高代码的复用性。      由 函数 来保证

弊端：
    代码量增加了，因为私有内容外界无法访问，
    必须提供公共的访问方式，代码量就增加了。
"""

class Prentice:
    # 3.1 属性
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
        self.__money = 20000

    # 3.2 方法
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    def get_money(self):#或许私有属性值get_xx
        return self.__money
    def set_money(self):#习惯私有属性值set_xx
        self.__money=100

# 4. 定义徒孙类
class TuSun(Prentice):
    pass


# 5. 测试
if __name__ == '__main__':
    ts = TuSun()
    print(ts.kongfu)
    ts.make_cake()
    #print(ts.__money) #报错，父类私有成员，子类无法访问

    print(ts.get_money())  #通过父类提供的公共的访问方式，访问父类的私有成员