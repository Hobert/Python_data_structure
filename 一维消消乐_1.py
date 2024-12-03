from pythonds.basic.stack import Stack
def fuc(my_str):
    s = Stack()
    for i in my_str:
        if not s.isEmpty() and i == s.peek():#相同就消
            s.pop()
        else: 
            s.push(i)
    if s.isEmpty():
        print("OK")
    else:
        print("False")
if __name__ == "__main__":
    fuc("))))(((())))")


