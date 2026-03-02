""" 
该文件用于 完成学生系统的 具体业务的操作，即：增删改查，保存学生信息。。。
"""
#导包
from student import Student
class StudentCMS:
    def __init__(self):
        self.stu_list=[]
    def show_menu(self):
        menu=""" 
************************************
本学员管理系统V2.0可完成如下操作:
    1.添加学员
    2.修改学员
    3.删除学员
    4.查询某个学员
    5.显示所有学员
    6.保存信息
    7.退出系统
*************************************
        """
        print(menu)
        
    def add_student(self):
        name=input("请输入学生姓名：")
        age=int(input("请输入学生年龄："))
        gender=input("请输入学生性别：")
        phone_number=input("请输入学生电话：")
        summary=input("请输入学生概述：")
        student=Student(name,age,gender,phone_number,summary)
        self.stu_list.append(student)
        print(f"{name}已经成功添加")
        
    def change_student(self):
        name=input("请输入你要修改的学生姓名：")
        for stu in self.stu_list:#enumerate = 带下标的遍历
            if stu.name==name:
                try:
                    stu.age = int(input("请输入修改后的学生年龄："))
                except ValueError:
                    print("年龄必须是数字！")
                    return
                stu.gender=input("请输入修改后的学生性别：")
                stu.phone_number=input("请输入修改后的学生电话：")
                stu.summary=input("请输入修改后的学生概述：")
                return
        print("这个学生并不在列表中")
    
    def del_student(self):
        name=input("请输入你要删除的学生姓名：")
        # for stu in self.stu_list:
        #     if stu.name==name:
        #         self.stu_list.remove(stu)
        #         print(f"{stu.name}已经被删除")
        #         return
        for i,stu in enumerate(self.stu_list):#enumerate = 带下标的遍历
            if stu.name==name:
                del self.stu_list[i]
                print(f"{name}已经被删除")
                return
        print("这个学生并不在列表中")
        
    def search_student(self):
        name=input("请输入你要查询的学生姓名：")
        for stu in self.stu_list:
            if stu.name==name:
                print(stu)
                return
        print("这个学生并不在列表中！")
        
    def show_all(self):
        if len(self.stu_list)==0:#if not self.stu_list:
            print("暂无学生信息，请添加后查询！")
        else:
            for stu in self.stu_list:
                print(stu)
            print()#为了格式好看加入换行
            
    def save(self):
        pass
    def load(self):
        pass
    def excute(self):
        while True:
            self.show_menu()
            user_input=input("请输入你的选项：")
            match user_input:
                case '1':
                    print("添加学生信息")
                    self.add_student()
                case '2':
                    print("修改学生信息")
                    self.change_student()
                case '3':
                    print("删除学生信息")
                    self.del_student()
                case '4':
                    print("查询某个学员")
                    self.search_student()
                case '5':
                    print("显示所有学生信息")
                    self.show_all()
                case '6':
                    print("保存信息")
                    self.save()
                case '7':
                    user_input=input("正在退出系统是否确认退出，请输入Y/N:")
                    if user_input.lower() == "y":
                        print("退出系统")
                        break
                    else:
                        print("继续使用")
                case _:
                    print("输入错误，请重新输入")
    




    
#测试
if __name__ == "__main__":
    cms=StudentCMS()
    #调用学生管理系统对象的start()函数，启动学生管理系统
    cms.excute()