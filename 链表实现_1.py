class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    
    def set_next(self,next):
        self.next = next 
    
    def set_data(self,data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next


#保存对空表的引用信息
#如果是空表的话，就将head设置为None
class Unorderlist:
    def __init__(self): 
        self.head = None

    #添加变量
    def add(self,data):
        temp = Node(data)#临时变量存储
        temp.set_next(self.head)#将原先位于无序表中的第一个数据设置为新加入表中的next
        self.head = temp#将表头设置为临时变量
    
    #测量大小
    def size(self):
        count = 0
        current = self.head
        while current != None:#这里要使用while,一直遍历到结尾
            count += 1
            current = current.get_next()
        return count 

    #找目标值
    def search(self,target):
        current = self.head
        for i in range(self.size()):
            if (current.get_data() != target):
                current = current.get_next()
            else:
                return True
        return False
    
    #删除目标值
    def remove(self,target):
        previous = None
        current = self.head
        for i in range(self.size()):
            if self.head.get_data() == target:#如果第一个即为目标值，则将head直接连为下一个节点即可
                self.head = current.get_next()
                return True
            if (current.get_data() != target):
                previous = current 
                current = current.get_next()
            elif current.get_data() == target:#找到了就直接设置为下一个节点即可
                self.previous.set_next() = current.get_next()
                return True
        return False