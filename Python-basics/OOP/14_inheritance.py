"""
继承：指子类继承父类的属性和方法-->指的是类的继承，不是对象的继承

案例：继承入门

继承介绍：
    概述：
        子类继承父类的属性和方法
    写法：
        class 子类名（父类名）：
            pass
    例如：
        class A(B):
            pass
    好处：
        提高代码的复用性
    弊端：
        耦合性增强了，父类不好的内容，子类想没有都不行
    扩展：开发原则
        高内聚，低耦合
        内聚：指的是类自己独立处理问题的能力
        耦合：指的是类与类之间的关系
"""
#需求：定义父类（男，散步），定义子类（继承父类）
class Father:
    def __init__(self):
        self.gender = 'male'
    def work(self):
        print("喜欢work")
    def __str__(self):
        return f'这是一个{self.gender}'
    
class Son(Father):
    pass

#测试
if __name__ == '__main__':
    c1=Son()
    c1.work()
    print(c1)

"""
案例：演示单继承，即：1 个子类继承自 1 个父类。

故事 1：一个煎饼的老师傅，在煎饼果子界摸爬滚打多年，研发了一套精湛的煎饼技术，师父要把这套技术传授给他的唯一的最得意的徒弟。

分析：
    1.定义师傅类，Master
        属性：kongfu
        行为：make_cake()

    2.定义子类，Prentice，继承师傅类。
"""
class Master():
    def __init__(self):
        self.peifang='古方煎饼配方'
    def make_pancake(self):
        print(f"采用{self.peifang}摊煎饼")
class Prentice(Master):
    pass

#测试
if __name__ == "__main__":
    p1=Prentice()
    p1.make_pancake()

"""
案例：演示多继承。

需求：小明是个爱学习的好孩子，想学习更多的煎饼果子技术，于是，在百度搜索到黑马程序员学校，报班来培训学习煎饼果子技术。


"""

class Master():
    def __init__(self):
        self.peifang='古方煎饼配方'
    def make_pancake(self):
        print(f"采用{self.peifang}摊煎饼")
class School():
    def __init__(self):
        self.peifang='学校煎饼配方'
    def make_pancake(self):
        print(f"采用{self.peifang}摊煎饼")
class Prentice(School,Master):#当一个类有多个父类是，默认使用第一个父类的同名属性和方法，可以使用 类名.__mro__属性 或者 类名.mro()方法查看调用的先后顺序  注释：MRO（method Resolution Order):方法解析顺序
    pass
#测试
if __name__ == "__main__":
    p1=Prentice()
    p1.make_pancake()

print(Prentice.mro())#[<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>]
print(Prentice.__mro__)#(<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>)