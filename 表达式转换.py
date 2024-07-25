#该表达式转换一定是建立在有括号的基础上的
from pythonds.basic.stack import Stack
def infixToPostfix(infixexpr):
    prec = {}
    #确定优先级
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    s = Stack()#创建空栈
    output_list = []#创建空列表
    #input_list = infixexpr.split
    for i in range(len(infixexpr)):        
        if ord(infixexpr[i]) >= 65 and ord(infixexpr[i]) <= 90:#取出操作数,直接加在输出列表
            output_list.append(infixexpr[i])
            #print(output_list)

        elif infixexpr[i] == "(":#如果是左括号就压入栈
            s.push(infixexpr[i])

        #主要是在下面这个条件判断产生错误
        # 首先需要有跳出循环的条件，在取到“）”时，将栈pop出来的第一个就是括号内需要的操作符    
            
        elif infixexpr[i] == ")":#如果是右括号就
            temper = s.pop()
            while temper != '(':#
                output_list.append(temper)
                temper = s.pop()#栈中操作符前的一定是左括号，触发跳出循环的条件
            #output_list.append(temper)
            
            #在每次括号匹配结束后都要对栈中留下的操作符进行一定的处理
            for i in range(len(s.items)):
                if (s.items[i] == "+" or s.items[i] == "/" or s.items[i] == "-" or s.items[i] == "*") and len(s.items)-1  >= i:
                    output_list.append(s.items[len(s.items) - i - 1])
        #如果是操作符且栈非空比较
        elif s.isEmpty() != True and (infixexpr[i] == "+" or infixexpr[i] == "/" or infixexpr[i] == "-" or infixexpr[i] == "*"):
            print(s.items)
            if prec[infixexpr[i]] >= prec[s.items[-1]] and s.items[-1] == "(":
                s.push(infixexpr[i])
            while prec[infixexpr[i]] < prec[s.items[-1]] :
                temper = s.pop()
                #output_list.append(infixexpr[i])
                output_list.append(temper)
            #s.push(infixexpr[i])
        
        #栈为空就将操作符压入
        elif s.isEmpty() == True and (infixexpr[i] == "+" or infixexpr[i] == "/" or infixexpr[i] == "-" or infixexpr[i] == "*"):
            s.push(infixexpr[i])

        print(s.items)
        print(output_list)

    #在对字符串进行完遍历之后，在对栈中剩余的操作符进行处理
    for i in range(len(s.items)):
        if (s.items[i] == "+" or s.items[i] == "/" or s.items[i] == "-" or s.items[i] == "*") and len(s.items)-1  >= i:
            output_list.append(s.items[len(s.items) - i - 1])
    
    print(output_list)
 
if __name__ == "__main__":
    infixToPostfix("K*(A+B)*C")
    infixToPostfix("A*B+C*D")