from timeit import Timer
from big_o import big_o,datagen
item  = 1
def list_process1():
    list.insert(0,item)
def list_process2():
    list.append(item)
for i in range(10000,100001,10000):
    list1 = list(range(i))
    t1 = Timer("list_process1","from __main__ import list_process1")
    print("process1_list的规模点为%d消耗的时间:"%i)
    print("cancat %f seconds\n" % t1.timeit(number=1000))

    t2 = Timer("list_process2","from __main__ import list_process2")
    print("process2_list的规模点为%d消耗的时间:"%i)
    print("cancat %f seconds\n" % t1.timeit(number=1000))
#list1 =  list(range(10000))
#t1 = Timer("list_process1","from __main__ import list_process1")
#print("cancat %f seconds\n" % t1.timeit(number=1000))

for i in range(10000,100001,10000):
    best , others = big_o(
        sorted,
        lambda n:datagen.integers(n,0,i),
        min_n = 0,
        max_n = i,
        n_measures = 1000)
    print(best)
