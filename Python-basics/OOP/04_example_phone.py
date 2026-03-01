"""
案例：定义手机类，能开机，关机，拍照
回顾：
    定义类的格式
        class 类名：
            #属性
            #行为
    访问 类中成员 的格式：
        类外：对象名. 的方式
        类外：self. 的方式
"""
class Cell:
    def on(self):
        print(f"{self}Open")
    def off(self):
        print(f"{self}Off")
    def pic(self):
        print(f"{self}pic")

c1 = Cell()
print(f"c1 object{c1}")
c1.on()
c1.off()
c1.pic()