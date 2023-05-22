#8.s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"

s = "ajldjlajfdljfddd"

unique_chars = list(set(s))

sorted_chars = sorted(unique_chars)

result = ''.join(sorted_chars)

print(result)  
