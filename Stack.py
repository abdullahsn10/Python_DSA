class Stack:
    def __init__(self):
        self.stack = []

    
    def push(self, data):
        self.stack.append(data)
    
    @property
    def size(self):
        return len(self.stack)
    

    def is_empty(self):
        return True if not self.size else False
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Can't Pop From Empty Stack")
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Empty Stack")
        
    


if __name__ == '__main__':
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
    