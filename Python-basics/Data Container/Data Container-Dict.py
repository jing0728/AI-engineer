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

# #遍历
# for k in dict1.keys():
#     print(f"{k}:{dict1[k]}")
    
# for k in dict1.items():
#     print(f"{k[0]}:{k[1]}")
    
# for k,v in dict1.items():
#     print(f"{k}:{v}")

#案例：购物车管理系统
# shopping_cart=dict()
# #添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# items = input("开始购物吧请输入你想要添加的产品： ")
# price = float(input("请输入价格: "))
# qty = int(input("请输入数量："))
# shopping_cart[items]=[price,qty]
# #修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# change = input("请问是否需要修改购物车？请输入是或否")
# if change == "是":
#     items = input("请输入你想要修改的产品：")
#     price = float(input("请输入价格: "))
#     qty = int(input("请输入数量："))
#     shopping_cart[items]=[price,qty]

# #删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# delte = input("请问是否需要删除购物车中的某样物品？请输入是或否")
# if delte == "是":
#     items = input("请输入你想要删除的产品：")
#     print(f"已经将{shopping_cart.pop(items)}从购物车内删除")

# #查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# for i,p,q in shopping_cart.items():
#     print(f"商品名称：{i},商品价格：{p},商品数量：{q}")
# shopping_cart=dict()
# print("欢迎来到XXX超市请开始你的购物之旅吧")
# while True:
#     choose = input("请问你想添加，修改，删除，查询，还是退出呢？\n请只输入修改，删除，查询，退出来进行购物谢谢:")
#     if choose == "添加":
#         items = input("请输入你想要添加的产品： ")
#         price = float(input("请输入价格: "))
#         qty = int(input("请输入数量："))
#         shopping_cart[items]=[price,qty]
#     elif choose == "修改":
#         items = input("请输入你想要修改的产品：")
#         price = float(input("请输入价格: "))
#         qty = int(input("请输入数量："))
#         shopping_cart[items]=[price,qty]
#     elif choose == "删除":
#         items = input("请输入你想要删除的产品：")
#         if items in shopping_cart:
#             shopping_cart.pop(items)
#             print(f"已经将{items}从购物车内删除")
#         else:
#             print(f"购物车里面没有{items}")
#     elif choose == "查询":
#         for name, (price, qty) in shopping_cart.items():
#             print(f"商品名称：{name}，商品价格：{price}，商品数量：{qty}，总金额是{sum(price * qty for price, qty in shopping_cart.values())}")
        
#     elif choose == "退出":
#         print
#         print("感谢您的购买，祝您生活愉快！！！")
#         break
#     else:
#         print("请输入正确的指令")
###列编辑快捷键：alt + shift