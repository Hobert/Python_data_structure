from pythonds.basic.deque import Deque

def word_judge(word):
    q = Deque()
    #不能直接将word使用add加入deque中,这样无法将字符串完全加入
    for i in word:
        q.addFront(i)

    while(q.size() > 1):
        temp1 = q.removeFront()
        temp2 = q.removeRear()
        if temp1 != temp2 :
            return False
    return True
if __name__ == "__main__":
    if word_judge("radar"):
        print("是回文词")
    else:
        print("不是回文词")