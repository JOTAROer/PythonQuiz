#6.列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]

my_list = [1, 2, 3, 4, 5]

squared_list = list(map(lambda x: x**2, my_list))
print(squared_list) 

filtered_list = [x for x in squared_list if x > 10]
print(filtered_list) 
