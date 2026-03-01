"""
案例：小明原始体重100kg，跑步一次减少0.5kg，每次胡吃海喝一次增加2kg
class Student():
    pass
属性：
current_weight=100kg

行为：
run()--> loss weight 0.5kg
eat()--> gain weight 2kg
"""
class Student():
    def __init__(self):
        self.current_weight=100
    def run(self):
        print('run')
        self.current_weight -=0.5
    def eat(self):
        print('eat')
        self.current_weight +=2
    def __str__(self):
        return f'current weight:{self.current_weight}'

if __name__ == '__main__':
    xm=Student()
    xm.run()
    xm.run()
    xm.eat()
    print(xm)