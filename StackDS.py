class Stack:
    def __init__(self):
        self.__stack = []
    
    def push(self, value):
        self.__stack.append(value)
    
    @property
    def size(self):
        return len(self.__stack)

    def pop(self):
        if self.size :
            return self.__stack.pop() 
        else:
            print("Can't Pop from empty stack")
    
    def top(self):
        if self.size:
            return self.__stack[-1]
        else:
            print("Can't get Top of empty stack")
    


def is_balanced_symbols(string):
    stack = Stack()

    opening_symbols = ['{', '[', '(', '<']
    closing_symbols = ['}', ']', ')', '>']
    symbols = ['{}', '[]', '()', '<>']

    for char in string:
        if char in opening_symbols:
            stack.push(char)
        elif char in closing_symbols:
            if not stack.size:
                return False
            elif stack.pop() + char not in symbols:
                return False
    return True if not stack.size else False

if is_balanced_symbols('(({[]}))'):
    print("Balanced")
else:
    print("NO")


