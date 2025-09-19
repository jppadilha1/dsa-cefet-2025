from stack import Stack

class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_in_stack = Stack()
    
    def push(self,val):
        if self.stack.is_empty() or val <= self.min_in_stack.peek():
            self.min_in_stack.push(val)
        
        self.stack.push(val)

    def pop(self):
        if self.stack.peek() == self.min_in_stack.peek():
            self.min_in_stack.pop()
        self.stack.pop()

    def top(self):
        top = self.stack.peek()
        print(top)
        return top
        
    def getMin(self):
        min = self.min_in_stack.peek()
        print(f'Current Min: {min}')
        return min

stack = MinStack()

stack.push(3)
stack.push(10)
stack.push(2)
stack.push(10)
stack.push(28)
stack.push(1)
stack.push(100) #top of stack
stack.getMin() #1
stack.pop()
stack.pop()
stack.getMin()#removi o 1 agora o mínimo é 2
stack.pop()
stack.pop()
stack.pop()
stack.getMin()#removi o 2 agora o mínimo é 3