from pythonds.basic.queue import Queue
def hotPotato(my_list,num):
    q = Queue()
    #下面在遍历queue时应该使用class_Queue中的方法，如果直接加等list类型的话，就会改变q对象的类型
    for index in my_list:
        q.enqueue(index)


        
    count = 0
    while q.size() != 1:

        if count != num:
            temp = q.dequeue()
            q.enqueue(temp)

        count += 1
        q.dequeue()
    print(q.dequeue())
if __name__ == "__main__":
    hotPotato(["Akebi","Komichi","Hobert"],5)

