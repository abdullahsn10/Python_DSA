class Queue:
    def __init__(self):
        self.queue = []
    

    def enqueue(self, item):
        self.queue.append(item)
    


    def is_empty(self):
        return True if not len(self.queue) else False
    
    def size(self):
        return len(self.queue)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Empty Queue")
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Empty Queue")
    


myQ = Queue()
myQ.enqueue(10)
myQ.enqueue(20)
myQ.enqueue(30)
myQ.enqueue(40)
print(myQ.size())
myQ.dequeue()
print(myQ.front())