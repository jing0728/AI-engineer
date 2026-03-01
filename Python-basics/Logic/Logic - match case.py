###模式匹配:match...case--用一个清晰的模板去精确匹配数据的结构和内容，匹配成功则执行响应的操作
day = input("输入星期几")
match day:
    case "1":
        print("周一")
    case "2":
        print("周二")
    case "3":
        print("周三")
    case "4":
        print("周四")
    case "5":
        print("周五")
    case "6"| "7":#其中的 | 表示或/or的关系，匹配多个模式中的任意一个
        print("周末")
    case _:# _ 匹配其他所有的情况
        print("输入错误")

# 案例：输入数字和运算符进行运算
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
simple = input("输入你想进行的运算模式： ")
match simple:
    case "+":
        print(f"num1是{num1}，num2是{num2}，进行的运算是{simple}，结果是{num1+num2}")
    case "/":
        print(f"num1是{num1}，num2是{num2}，进行的运算是{simple}，结果是{num1/num2}")
    case "-":
        print(f"num1是{num1}，num2是{num2}，进行的运算是{simple}，结果是{num1-num2}")
    case "*":
        print(f"num1是{num1}，num2是{num2}，进行的运算是{simple}，结果是{num1*num2}")
    case _:
        print("没有办法进行运算哦")

#案例：游戏指令系统
move = input("请输入你的动作： ")
match move:
    case "上"|"w"|"W":
        print("角色向上移动")
    case "下"|"s"|"S":
        print("角色向下移动")
    case "左"|"a"|"A":
        print("角色向左移动")
    case "右"|"d"|"D":
        print("角色向右移动")
    case "跳"|" ":
        print("角色跳跃")
    case "攻击"|"j"|"J":
        print("角色发动攻击")
    case "推出"|"esc"|"ESC":
        print("角色退出游戏")
    case _:
        print("指令错误")