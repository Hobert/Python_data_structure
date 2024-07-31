#实现原理是以用户每次取盘子来对洗盘子进行调整
from pythonds.basic.stack import Stack
s = Stack()
i = 0 #字符下标
n = 0 #洗碗
k = 0 #客户取碗
my_str = input()
#实现遍历最多10次轮序吗？
while n < 10 and k < 10:
    k = int(my_str[i])
    if n <= k:
        for ret in range(n,k+1):
            s.push(ret)
        n = k+1
    #下面的这个while用来判断每次洗的最后一个或上次取盘后剩的最上面的盘子是否与取盘一致
    while not s.isEmpty() and int(s.peek()) == int(my_str[i]):#这里peek使用记得加括号
        s.pop()
        i += 1
if  s.isEmpty():
    print("True")
else:
    print("False")