###set-集合-自动去重
#基本操作
# 无序的,不可重复,可修改的数据容器
# 定义集合
s1={'c','d','x','t','o','u'}
#定义空集合
s2=set()#不可以用{},{}是用来定义空字典的

#常用方法
s1 ={100,200,300,400,500,600,700,800}
#add()-->添加元素到集合中
s1.add(1200)
print(s1)#{800, 100, 200, 300, 400, 1200, 500, 600, 700}
#remove()-->移除集合中的指定元素
s1.remove(800)
print(s1)#{100, 200, 300, 400, 1200, 500, 600, 700}
#pop()-->速记删除集合中的元素并返回
e = s1.pop()
print(e)#100
print(s1)#{200, 300, 400, 1200, 500, 600, 700}
# #clear()-->清空集合
# s1.clear()
# print(s1)#set()
#differnece()-->求两个集合的差集(包括在第一个集合但不在第二个集合的元素)
s2 = {100,500,700,800,900,1000}
print(s1.difference(s2))#{200, 300, 400, 1200, 600}
print(s2.difference(s1))#{800, 900, 100, 1000}
#union()-->求取两个集合的合集
print(s2.union(s1))#{800, 100, 900, 1000, 200, 300, 400, 1200, 500, 600, 700}
print(s1.union(s2))#{800, 100, 900, 1000, 200, 300, 400, 1200, 500, 600, 700}
#intersection()-->求取两个集合的交集--可以用&来替代---s1&s2
print(s2.intersection(s1))#{700, 500}
print(s1.intersection(s2))#{700, 500}

#案例：选课
# 选修足球学生名单
football_set = {
    "王林", "曾牛", "徐立国", "遁天", "天运子",
    "韩立", "厉飞雨", "乌丑", "紫灵"
}

# 选修篮球学生名单
basketball_set = {
    "张铁", "墨居仁", "王林", "姜老道",
    "曾牛", "王蝉", "韩立", "天运子",
    "李化元", "厉飞雨", "云露"
}

# 选修法语学生名单
french_set = {
    "许木", "王卓", "十三", "虎咆", "姜老道",
    "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"
}

# 选修艺术学生名单
art_set = {
    "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"
}

# print(f"同时选修了法语和艺术的学生是: {art_set.intersection(french_set)}")
#intersection 可以用&来表示
print(f"同时选修了法语和艺术的学生是: {art_set&french_set}")
# print(f"同时选修四门课的学生是：{football_set.intersection(basketball_set.intersection(french_set.intersection(art_set)))}")
print(f"同时选修四门课的学生是：{football_set&basketball_set&french_set&art_set}")
#different 可以用-
# print(f"选修了足球但是没有选修篮球的学生是：{football_set.difference(basketball_set)}")
print(f"选修了足球但是没有选修篮球的学生是：{football_set-basketball_set}")
#集合推导式，语法{要往集合中添加的数据 for s in set1 if条件}
fb_set={s for s in football_set if s not in basketball_set}
print(f"选修了足球但是没有选修篮球的学生是：{fb_set}")
#并集（|）
student = (football_set | basketball_set | art_set |french_set)
# student =football_set.union(basketball_set.union(french_set.union(art_set)))

# for name in student:
#     i = 0
#     if name in french_set:
#         i+=1
#     if name in basketball_set:
#         i+=1
#     if name in football_set:
#         i+=1
#     if name in art_set:
#         i+=1
#     print(f"{name}一共修了{i}门课程")

# #更加好的写法
# for name in student:
#     count=sum([
#         name in football_set,
#         name in basketball_set,
#         name in french_set,
#         name in art_set
#     ])
#     print(f"{name}一共修了{count}门课程")

# #List写法
# courses =[football_set,basketball_set,french_set,art_set]
# for name in student:
#     count = sum(name in course for course in courses) #sum(True, False, True, False) = 2,利用布尔值进行相加
#     print(f"{name}一共修了{count}门课程")
    
#解包写法
courses = [*football_set,*basketball_set,*french_set,*art_set]
for name in student:
    print(f"{name}一共上了{courses.count(name)}门课程")