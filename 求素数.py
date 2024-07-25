from math import sqrt
a = int(input("请输入一个数："))
for i in range(2,int(sqrt(a))+1):
    if a%i == 0:
        print("该数不是素数")
        break
else:    #利用for ... else... 可以减少flag变量，条件判断的使用
       print("该数是素数")

# # 1既不是素数也不是合数
# #可以用flag做标志位
# b = int(input("请输入一个数："))
# Flag = False
# for i in range(2,b):
#     if b%i == 0:
#         Flag = True

# if Flag:
#     print("是合数")

# else:
#     print("是素数")