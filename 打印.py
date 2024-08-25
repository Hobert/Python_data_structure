from pythonds.basic.queue import Queue
import random
class Printer:
    def __init__(self,ppm):
        self.pagerate = ppm#单位每分钟打印的页数
        self.currentTask = None 
        self.timeRemaining = 0
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1#倒计时
            if self.timeRemaining <= 0:
                self.currentTask = None
    def busy(self):
        if self.currentTask == None:
            return False
        else:
            return True   
    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate#计算每个作业任务的倒计时

class Task():
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self,currenttime):
        return currenttime - self.timestamp
    
def newprintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False
    
def simulation(pagesperMinute,numSenconds):
    printer = Printer(pagesperMinute)
    
    printQueue = Queue()
    
    waitingtime = []

    for currenttime in range(numSenconds):
        if newprintTask():
            newtask = Task(currenttime)
            printQueue.enqueue(newtask)
            
        if(printer.busy() == False) and (printQueue.isEmpty() == False):
            printer.startNext(printQueue.dequeue())
            waitingtime.append(newtask.waitTime(currenttime))
        
        printer.tick()

    averageWait = sum(waitingtime)/len(waitingtime)
    print("Averagewait %6.2f s  %3d tasks wait"%(averageWait,printQueue.size()))
         

if __name__ == "__main__":

    for i in range(10):

        simulation(20,3599)

