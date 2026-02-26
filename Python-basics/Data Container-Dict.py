####字典
# #通过【字/词语】，找到该字对应的【解释】
# #每个【字/词语】对应一个解释，【字/词语】是不可以重复的
# #dict里面储存的键值对(key:value)类型的数据，可以根据键(key)找到对应的值(value)
# dict1={"王良":678,"韩立":700}
# print(dict1)
# #定义空字典
# #字典名称={}
# #字典名称=dict()
# #key不可以重复，如果重复的后面的值覆盖前面的值

# #访问
# print(dict1["王良"])

# #修改
# dict1["王良"]=688
# print(dict1)
dict1={"王良":678,"韩立":700}
# #添加
# #字典名称[key] = value-->往指定字典中添加key-value键值对
# dict1["张三"]=789
# print(dict1)

# #删除
# #字典名称.pop(key) -->删除字典中指定的key值，并返回该key对应的value
# #del 字典名称[key] -->删除字典中指定的key值
# dict2 = dict1.pop("王良")
# del dict1["韩立"]
# print(dict2)
# print(dict1)
# #修改
# #字典名称[key] =value -->删除字典中指定的键值对
# dict1["张三"]=778
# print(dict1)
# #字典名称[key] --> 根据key获取value
# print(dict1["张三"])
# #字典名称.get(key) --> 根据key获取value
# print(dict1.get("张三"))

# #查询
# #字典名称.keys() --> 获取所有的key
# print(dict1.keys())
# #字典名称.values() --> 获取所有的value
# print(dict1.values())
# #字典名称.items() --> 获取所有的key-value键值对
# print(dict1.items())

#遍历
for k in dict1.keys():
    print(f"{k}:{dict1[k]}")
    
for k in dict1.items():
    print(f"{k[0]}:{k[1]}")
    
for k,v in dict1.items():
    print(f"{k}:{v}")