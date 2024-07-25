#十进制转换为其他进制同理，将除数换成对应的就可以了
#自解
from pythonds.basic.stack import Stack
def transform(number):
    s = Stack()
    buffer = ""
    while number / 2 != 0 and number / 2 >= 1:#number > 0即可
        print(int(number))
        number = int(number)
        ret = number % 2
        s.push(ret)
        if (number/2) < 2 :
            break
        number = number / 2#更新number
        
    print(s.items)
    s.push("1")
    while s.isEmpty() == False:
        buffer += str(s.pop())#这里需要将其转换为字符
    print(buffer)
if __name__ == "__main__":
    transform(233)



#他解
from pythonds.basic.stack import Stack
def divideBy2(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2#求出余数
        remstack.push(rem)
        decNumber = decNumber // 2#实现整除2
    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())
    return binString
print(divideBy2(233))