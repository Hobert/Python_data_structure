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
class Orderedlist:
    def __init__(self): 
        self.head = None

    #添加变量
    def add(self,data):
        temp = Node(data)   #临时变量存储
        previous = None 
        stop = False
        current = self.head
        found = False
        while current != None and not stop:
            if current.get_data() < data:#检测到小就继续下移
                previous = current
                current = current.get_next()
            else:
                stop = true
        if previous == None:
            temp.set_next(self.head)
        else:
            previous.set_next(temp)
            temp.set_next(current)
        
        
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
        found = False
        while not found:
            if current.get_data() == target:
                return True
            else:
                current = current.get_next()
            if current.get_data() > target:#如果后面的数全部大于目标值，则直接跳出查询，节省时间
                return False
        return False
    
    #删除目标值
    def remove(self,target):
        previous = None
        current = self.head
        for i in range(self.size()):
            if (current.get_data() != target):
                previous = current 
                current = current.get_next()
            elif current.get_data() == target:#找到了就直接设置为下一个节点即可
                previous.set_next(current.get_next())
                return True
            
        if previous == None:
            self.head = current.get_next()

        return False
    
    #判断是否为空表
    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False