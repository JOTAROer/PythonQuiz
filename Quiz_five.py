#5.fun(*args,**kwargs)中的*args,**kwargs什么意思？

#在Python中，`*args`和`**kwargs`是用于函数定义中的特殊参数形式。
#`*args`用于传递可变数量的非关键字参数（位置参数），它允许函数接受任意数量的参数，并将它们作为一个元组（tuple）传递给函数。在函数内部，我们可以通过遍历`args`来访问这些参数
# `**kwargs`用于传递可变数量的关键字参数，它允许函数接受任意数量的关键字参数，并将它们作为一个字典（dictionary）传递给函数。在函数内部，我们可以通过字典的键值对来访问这些参数。
#下面是一个示例，说明如何在函数中使用`*args`和`**kwargs`：

def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)
my_function(1, 2, name='John', age=30)