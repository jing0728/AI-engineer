####python模块--模块是python程序的基本组织单位。在模块中可以定义变量，函数，类，以及可以执行的代码

# ####导入模块-一般写在py文件的开头
# #import 模块名 —— import random,os -->调用方式：模块名，功能名
# import random
# print(random.randint(1,100))
# #import 模块名 as 别名 —— import random as rd -->调用方式：别名，功能名
# import random as rd
# print(rd.randint(1,100))
# #from 模块名 import 功能名 —— from random import randint,choice -->调用方式：功能名f
# from random import randint
# print(randint(1,100))
# #from 模块名 import 功能名 as 别名—— from random import randint as hoice -->调用方式：别名
# from random import randint as rt
# print(rt(1,100))
# #from 模块名 import * —— from random import* -->调用方式：功能名
# from random import*
# print(randint(1,100))

    
####自定义模块
# #模块名字就是py文件的名字
# import Data_Container_Project#导入自定义模块
# Data_Container_Project.subject_stats#使用模块中的功能
# #__name__ -->内置变量：表示当前模块的名字
# #测试代码-这段代码只有在当前文件时才会进行运算
# #__all__是一个模块级别的特殊变量，用于指定 from 模块名 import * 时会导入哪些功能（*通配了哪些功能）//private
# if __name__=='__mian__':
#     Data_Container_Project.subject_stats

####软件包（package）