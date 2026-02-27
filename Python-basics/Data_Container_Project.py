#开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
#1．添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
#2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
#3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。 
#4．查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
#5．列出所有学生：遍历所有学生信息并输出。
#6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
#7．退出系统。
# memu = """
# ######################################################################################################################
# # 1.添加学生信息    2.修改学生信息    3.删除学生信息    4.查询学生信息    5.列出所有学生信息    6.统计班级成绩    7.退出系统 #
# ######################################################################################################################
# """
# student={}
# #student={name:{"语文"：成绩,"数学":成绩,"英语":成绩}}
# while True:
#     print(memu)
#     choose =input("请选择你要进行的操作（1-7）：")
#     match choose:
#         case '1':
#             name = input("请输入想要录入的学生姓名： ")
#             if name in student:
#                 print("{name}已经在系统里面了")
#                 continue
#             chinese = float(input(f"请输入{name}的语文成绩： "))
#             math = float(input(f"请输入{name}的数学成绩： "))
#             english = float(input(f"请输入{name}的英语成绩： "))
#             student[name] = {"chinese": chinese, "math": math, "english": english}
#             print(f"{name}的信息已经录入系统了！")
#         case '2':#修改学生信息
#             name = input("请输入修改录入的学生姓名： ")
#             if name not in student:
#                 print("{name}不在系统里面了")
#                 continue
#             chinese = float(input(f"请修改{name}的语文成绩： "))
#             math = float(input(f"请修改{name}的数学成绩： "))
#             english = float(input(f"请修改{name}的英语成绩： "))
#             student[name] = {"chinese": chinese, "math": math, "english": english}
#             print(f"{name}的信息已经修改了！")
#         case '3':#删除学生信息
#             name = input(f"请输入想要删除的学生姓名： ")
#             if name not in student:
#                 print("{name}不在系统里面了")
#             else:
#                 student.pop(name)
#                 print(f"{name}的信息已经删除了！")
#         case '4':#查询学生信息
#             name = input(f"请输入想要查询的学生姓名： ")
#             for name in student:
#                 print(f"{name}的语文成绩是：{chinese}，数学成绩是：{math}，英语成绩是：{english}")
#         case '5':#列出所有学生信息
#             for name in student:
#                 print(student(name))
#         case '6':#统计班级成绩
#             #key=lambda = 指定“比较规则”
#             # print(
#             #     f"语文的最高分是：{max(info['chinese'] for info in student.values())}，{max(student, key=lambda name: student[name]['chinese'])}"
#             #     f"最低分是：{min(info['chinese'] for info in student.values())}，"
#             #     f"平均分是：{sum(info['chinese'] for info in student.values()) / len(student):.2f}"
#             # )
#             # print(
#             #     f"数学的最高分是：{max(info['math'] for info in student.values())}，{max(student, key=lambda name: student[name]['math'])}"
#             #     f"最低分是：{min(info['math'] for info in student.values())}，"
#             #     f"平均分是：{sum(info['math'] for info in student.values()) / len(student):.2f}"
#             # )
#             # print(
#             #     f"英语的最高分是：{max(info['english'] for info in student.values())}，{max(student, key=lambda name: student[name]['english'])}"
#             #     f"最低分是：{min(info['english'] for info in student.values())}，"
#             #     f"平均分是：{sum(info['english'] for info in student.values()) / len(student):.2f}"
#             # )
#             def subject_stats(students, subject_key, subject_name):
#                 if not students:
#                     print("暂无学生数据")
#                     return

#                 # 最高分学生
#                 max_name = max(students, key=lambda name: students[name][subject_key])
#                 max_score = students[max_name][subject_key]

#                 # 最低分学生
#                 min_name = min(students, key=lambda name: students[name][subject_key])
#                 min_score = students[min_name][subject_key]

#                 # 平均分
#                 avg_score = sum(info[subject_key] for info in students.values()) / len(students)

#                 print(f"{subject_name}最高分：{max_score}（{max_name}）")
#                 print(f"{subject_name}最低分：{min_score}（{min_name}）")
#                 print(f"{subject_name}平均分：{avg_score:.2f}")
#             subject_stats(student, "chinese", "语文")
#             subject_stats(student, "math", "数学")
#             subject_stats(student, "english", "英语")
#         case '7':#退出系统
#             print("Bye bye~")
#             break
#         case _:
#             print("输入错误，请重新选择")

memu = """
######################################################################################################################
# 1.添加学生信息    2.修改学生信息    3.删除学生信息    4.查询学生信息    5.列出所有学生信息    6.统计班级成绩    7.退出系统 #
######################################################################################################################
"""

student = {}
# student = {name: {"chinese": 成绩, "math": 成绩, "english": 成绩}}

def subject_stats(students, subject_key, subject_name):
    if not students:
        print("暂无学生数据")
        return

    max_name = max(students, key=lambda n: students[n][subject_key]) #key=lambda = 指定“比较规则”
    min_name = min(students, key=lambda n: students[n][subject_key])

    max_score = students[max_name][subject_key]
    min_score = students[min_name][subject_key]
    avg_score = sum(info[subject_key] for info in students.values()) / len(students)

    print(f"{subject_name}最高分：{max_score}（{max_name}）")
    print(f"{subject_name}最低分：{min_score}（{min_name}）")
    print(f"{subject_name}平均分：{avg_score:.2f}")

while True:
    print(memu)
    choose = input("请选择你要进行的操作（1-7）：").strip() #.strip() = 去掉字符串两边的空白字符
    #   print(s.lstrip())  # 左
    #   print(s.rstrip())  # 右
    #   print(s.strip())   # 两边

    match choose:
        case '1':  # 添加学生信息
            name = input("请输入想要录入的学生姓名： ").strip()
            if name in student:
                print(f"{name}已经在系统里面了")
                continue

            chinese = float(input(f"请输入{name}的语文成绩： "))
            math = float(input(f"请输入{name}的数学成绩： "))
            english = float(input(f"请输入{name}的英语成绩： "))

            student[name] = {"chinese": chinese, "math": math, "english": english}
            print(f"{name}的信息已经录入系统了！")

        case '2':  # 修改学生信息
            name = input("请输入想要修改的学生姓名： ").strip()
            if name not in student:
                print(f"{name}不在系统里面")
                continue

            chinese = float(input(f"请修改{name}的语文成绩： "))
            math = float(input(f"请修改{name}的数学成绩： "))
            english = float(input(f"请修改{name}的英语成绩： "))

            student[name] = {"chinese": chinese, "math": math, "english": english}
            print(f"{name}的信息已经修改了！")

        case '3':  # 删除学生信息
            name = input("请输入想要删除的学生姓名： ").strip()
            if name not in student:
                print(f"{name}不在系统里面")
            else:
                student.pop(name)
                print(f"{name}的信息已经删除了！")

        case '4':  # 查询学生信息
            name = input("请输入想要查询的学生姓名： ").strip()
            info = student.get(name) #字典名称.get(key) --> 根据key获取value
            if not info: #if info is None:
                print(f"未找到学生：{name}")
            else:
                print(f"{name}的语文成绩是：{info['chinese']}，数学成绩是：{info['math']}，英语成绩是：{info['english']}")

        case '5':  # 列出所有学生信息
            if not student:
                print("暂无学生信息")
            else:
                print("==== 所有学生信息 ====")
                for name, info in student.items():
                    print(f"{name}：语文 {info['chinese']}，数学 {info['math']}，英语 {info['english']}")

        case '6':  # 统计班级成绩
            subject_stats(student, "chinese", "语文")
            subject_stats(student, "math", "数学")
            subject_stats(student, "english", "英语")

        case '7':  # 退出系统
            print("Bye bye~")
            break

        case _:
            print("输入错误，请重新选择")

if __name__=='__mian__':
    subject_stats()