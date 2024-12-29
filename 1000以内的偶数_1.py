#第一种方法
list1 = []
for i in range(1,1001):
    if i%2==1:
        list1.append(i)
print(list1)
print("\n")
#第二种方法
list2 = []
for i in range(1,100,2):
    list2.append(i)
print(list2)