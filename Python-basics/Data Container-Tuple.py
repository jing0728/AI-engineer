####元组（Tuple)--一旦定义完成，不可被修改(类似与列表)

# #定义
# #元组名称 = (元素1，元素2，...)
# t1 =(1,2,3,4,5,6,80,50,156,123,546,6454,5)
# print(type(t1))
# #元组名称 = ()
# #元组名称 = tuple()
# #如果定义单个元素的元组，只要在后面加上，就可以了
# t2 = (100,)
# print(type(t2))
# #方法
# #count():统计元素在元组中出现的次数
# #index():查找某个元素所在的索引位置（第一次出现的位置）

# #组包与解包
# #组包：将多个值合并到一个容器当中
# #解包：将容器解开成独立的元素，分别赋值给多个变量
# t1=5,7,9,1
# #基础解包
# a,b,c,d = t1
# print(a)
# print(b)
# print(c)
# print(d)

# #扩展解包 数据生成为列表
# x,*y,z=t1 #x=5,y=7,9,z=1
# s,*o=t1 #s=5 o=7,9,1
# *o,e=t1 #o=5,7,9 e=1

# #变量值互换
# a=10
# b=20
# a,b=b,a
# print(a,b)
#逻辑链条
# #元组t得了组包，有了b,a值
# t=b,a
# #这步就是进行了解包，a，b被元组t赋值了
# a,b=t
# print(a,b)

# #变量值互换
# a=100
# b=200
# c=300
# a,b,c=c,a,b
# print(a,b,c)

#案例：计算每个学生的平均分，总分；统计各科最低分，最高分；找出平均分大于90的学生
student=(
    ('s01','Lin',85,92,78),
    ('s02','Li',92,88,95),
    ('s03','shi',78,85,82),
    ('s04','zen',88,79,91),
    ('s05','zhou',95,96,89),
    ('s06','wang',76,82,77),
    ('s07','hong',89,91,94),
    ('s08','xu',75,69,82),
    ('s09','mu',86,89,98),
    ('s10','tian',66,59,72)
    )
print("学号\t姓名\t语文\t数学\t英语\t总成绩\t平均分")
# #方式一
# for s in student:
#     total=s[2]+s[3]+s[4]
#     avg=total/3
#     print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{total}\t{avg:.1f}")

# #方式2
# for id,name,chinese,math,english in student:
#     total = chinese+math+english
#     avg=total/3
#     print(f"{id}\t{name}\t{chinese}\t{math}\t{english}")
    
# chinese=[s[2] for s in student]
# print(f"语文最低分是{min(chinese)},最高分是{max(chinese)},平均分{sum(chinese)/len(chinese)}")
# math=[s[3] for s in student]
# print(f"数学最低分是{min(math)},最高分是{max(math)},平均分{sum(math)/len(math)}")
# english=[s[4] for s in student]
# print(f"英语最低分是{min(english)},最高分是{max(english)},平均分{sum(english)/len(english)}")
    
  
# for s in student:
#     total=s[2]+s[3]+s[4]
#     avg=total/3
#     if avg>=90:
#         print(f"{s[1]}是优秀学生")
        
