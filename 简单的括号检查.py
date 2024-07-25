
#自解
#太抽象了，s.isEmpty()没有打括号,查了半天,无论进行什么判断都是False
from pythonds.basic.stack import Stack
Flag = True
def parchecker(symbolString):
    #Stack内部已经设置好初始值为空列表
    s = Stack()
    balance = True
    i = 0
    #print(symbolString)
    while i < len(symbolString):
        #匹配逻辑
        if symbolString[i] == "(":
            s.push(symbolString[i])
        elif symbolString[i] == ")" and s.isEmpty() == False:
            s.pop()
        #余出逻辑
        #可以检测右括号多余
        elif  symbolString[i] == ")" and s.isEmpty() == True:
            Flag = False
        i += 1
        #print(s.items)
    if s.isEmpty() == True :
        print("匹配")
    elif s.isEmpty() == False:#可以检测左括号多余
        print("不匹配")
    #print(s.isEmpty() == True)
if __name__ == "__main__":
    parchecker("()")
    #print("Akebi")


#他解
"""
from pythonds.basic.stack import Stack 
def parChecker(symbolString):
    s = Stack()
    balanced=True
    index=0
    print(symbolString[3])
    print(symbolString[3] == ")")
    while index < len(symbolString)and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index +1
    if balanced and s.isEmpty():
        return True
    else:
        return False
print(parChecker("()()())))"))
"""
