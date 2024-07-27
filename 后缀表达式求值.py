from pythonds.basic.stack import Stack
def get_value(my_str):
    s = Stack()
    for i in my_str:
        if i in "0123456789":
            s.push(i)
        if i == "+" or i == "-" or i == "*" or i == "/":
            temp1 = int(s.pop())
            temp2 = int(s.pop())
            if i == "+":
                s.push(temp2+temp1)
            if i == "-":
                s.push(temp2-temp1)
            if i == "*":
                s.push(temp2*temp1)
            if i == "/":
                s.push(temp2/temp1)
    return int(s.pop())
if __name__ == "__main__":
    print(get_value("65+2*"))