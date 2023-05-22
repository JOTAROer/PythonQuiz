#3.字典如何删除键和合并两个字典  
#del和update方法

my_dict = {'a': 1, 'b': 2, 'c': 3}
#删除单个建
del my_dict['a']

print(my_dict)  
#删除多个键
keys_to_delete = ['b', 'c']
for key in keys_to_delete:
    del my_dict[key]

print(my_dict) 


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# 使用update()方法合并两个字典
dict1.update(dict2)

print(dict1) 
