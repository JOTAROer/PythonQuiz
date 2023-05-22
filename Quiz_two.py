#2、如何在一个函数内部修改全局变量   利用global在函数声明 修改全局变量
count=0
def increment():
    global count
    count += 1

print(count)
increment()
print(count)