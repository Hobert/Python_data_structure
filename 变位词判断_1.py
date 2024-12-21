a = "pythoe"
b = "typhon"
# def judgement(a,b):
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if a[i] == b[j]:
#                 break
#             elif a[i] == b[j] and i == len(a)-1:
#                 return True
#             elif j == len(a)-1 and a[i] != b[j]:
#                 return False
# if judgement(a,b) == True:
#     print("是变位词")
# elif judgement(a,b) == False:
#     print("不是变位词")
# print("Akebi")

# list1 = list(b)
# print(list1)
# def judge(a,b):
#     for i in range(len(a)):
#        for j in range(len(a)):
#             if a[i] == b[j]:
#                 list1[j] = None
#                 break
#     for i in range(len(a)):
#         list1[i] == None
#         if list1[i] != None:
#             return False
#     return True
# if judge(a,b) == True:
#     print("是变位词")
# elif judge(a,b) == False:
#     print("不是变位词")



# def judge(a,b):
#     list1 = list(a)
#     list2 = list(b)
#     j = len(list2)
#     list1.sort()
#     list2.sort()
#     for i in range(len(list1)):
#         if list1[i] == list2[i]:
#             pass
#         else:
#             return False
#     return True
# if judge(a,b) == True:
#     print("是变位词")
# elif judge(a,b) == False:
#     print("不是变位词")



# for i in len(list):
#     for j in range(1,len(list)):
#         while j>i:
#             if list1[i] > list1[j]:
#                 temple = list1[j]
#                 list1[i+1] = list1[i]
#                 list1[i] = temple


"""计数比较-自解"""
dict1 = dict()
dict2 = dict()
list1 = list(a)
list2 = list(b)

for i in range(ord("a"),ord("z")+1):
    dict1[i] = 0

for i in range(ord("a"),ord("z")+1):
    dict2[i] = 0

def judge(a,b):
    for j in range(len(a)):
        for i in range(ord("a"),ord("z")+1):
            if ord(list1[j]) == i:
                dict1[i] = dict1[i] + 1
    for j in range(len(a)):
        for i in range(ord("a"),ord("z")+1):
            if ord(list2[j]) == i:
                dict2[i] = dict2[i] + 1
    for i in range(ord("a"),ord("z")+1):
        if dict1[i] == dict2[i]:
            pass
        else:
            return False
    return True
if judge(a,b) == True:
    print("是变位词")
elif judge(a,b) == False:
    print("不是变位词")


"""计数比较-他解"""
def judge(a,b):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(a)):
        pos = ord(a[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(a)):
        pos = ord(b[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    for i in range(26):
        if c1[i] == c2[i]:
            pass
        else:
            return False
    return True
if judge(a,b) == True:
    print("是变位词")
elif judge(a,b) == False:
    print("不是变位词")

