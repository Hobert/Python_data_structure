from timeit import Timer
def my_fuc():
    print("Akebi天下第一")
t1 = Timer("my_fuc()","from __main__ import my_fuc")#这里的__main__是告诉Python已经在前面定义过该函数了,当然也可以直接从其他包里导入
print("concat %f seconds\n" % t1.timeit(number= 100))
""""
这段代码是用Python编写的，它定义了一个名为`t1`的`Timer`对象。`Timer`是Python的`timeit`模块中的一个类，用于测量代码的执行时间。

`Timer`对象有两个参数：第一个参数是要测量执行时间的代码，第二个参数是代码所在的模块。在这个例子中，我们测量的是`my_fuc()`函数的执行时间，该函数位于`main`模块中。

`Timer`对象会自动计算出代码的执行时间，并将其存储在`t1`对象中。我们可以使用`t1.timeit()`方法来获取代码的执行时间，例如：

```Python
print(t1.timeit())
```

这将输出`my_fuc()`函数的执行时间。注意，`Timer`对象只能用于测量代码的执行时间，不能用于其他用途。
"""
