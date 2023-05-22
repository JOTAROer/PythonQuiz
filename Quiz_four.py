#4、python实现列表去重的方法  

#1. 使用集合（set）：将列表转换为集合，集合的特性是元素唯一，然后再将集合转换回列表。

my_list = [1, 2, 2, 3, 3, 4, 5, 5]
unique_list = list(set(my_list))
print(unique_list)

#2. 使用列表推导式：通过列表推导式遍历列表，并只保留第一次出现的元素。

my_list = [1, 2, 2, 3, 3, 4, 5, 5]
unique_list = [x for i, x in enumerate(my_list) if x not in my_list[:i]]
print(unique_list)

#3. 使用`dict.fromkeys()`方法：将列表的元素作为字典的键，并创建一个新字典，然后将字典的键转换回列表。

my_list = [1, 2, 2, 3, 3, 4, 5, 5]
unique_list = list(dict.fromkeys(my_list))
print(unique_list)