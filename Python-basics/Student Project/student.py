""" 
该文件用于记录 学生类，学生的属性信息为：姓名，年龄，性别，手机号，概述信息
"""
class Student():
    def __init__(self,name,age,gender,phone_number,summary):
        """_summary_用于初始化学生信息
        Args:
            name (_str_): _description_students's name
            age (_int_): _description_students's age
            gender (_str_): _description_students's gender
            phone_number (_str_): _description_students's phone_number
            summary (_str_): _description_students's summary
        """
        self.name=name
        self.age=age
        self.gender=gender
        self.phone_number=phone_number
        self.summary=summary
    def __str__(self):
        return f"学生姓名为：{self.name}，学生年龄为：{self.age}，学生性别为：{self.gender}，学生的手机号是：{self.phone_number}，学生的基本概述是：{self.summary}"
    
#测试
if __name__=="__main__":
    s1=Student('jing',24,"female",'123456',"good")
    print(s1)
    
        