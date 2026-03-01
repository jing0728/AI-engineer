"""
案例：烤地瓜
        0-3分钟-->生的
        3-7分钟-->半生不熟
        7-12分钟-->熟了
        超过12分钟-->已经烤焦，糊了
        可以按顾客意愿来添加调料
class Sweet_potato():
    pass
属性：
地瓜状态，调料，时间-->cook_status,cook_time,condiments
行为：
cook()-->烘烤
add()-->添加调料
"""
class Sweet_Potato():
    def __init__(self):
            self.cook_status="生的"
            self.cook_time= 0
            self.condiments = []
    def cook(self,time):
        self.cook_time += time
        if self.cook_time <= 3:
            self.cook_status = "生的"
        elif self.cook_time <= 7:
            self.cook_status = "半生不熟"
        elif self.cook_time <= 12:
            self.cook_status = "熟了"
        else:
            self.cook_status = "已经烤焦，糊了"
    def add(self,condiment):
        self.condiments.append(condiment)
    def __str__(self):
        return f'这个地瓜考了{self.cook_time}分钟,是{self.cook_status},加了{self.condiments}'

#测试
if __name__ == "__main__":
    sw =Sweet_Potato()
    sw.cook(5)
    sw.add("辣椒")
    print(sw)