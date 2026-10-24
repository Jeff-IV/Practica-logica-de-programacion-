
# Pila / stack

class Stack:
    
    def __init__(self):
        self.stack = []
        self.first = None
        
    def push(self, element):
        self.stack.append(element)
        self.first = element
        
        
    def pop(self):
        return self.stack.pop(-1)
    
    
    def peek(self):
        return self.first
    
    
    def is_empty(self) -> bool | int:
        return len(self.stack) == 0
    
    
    def size(self) -> int:
        return len(self.stack)
    
    def clear(self): 
        self.stack = []
        
        
stack = Stack()

for i in range(0, 5):
    stack.push(i)
    
for _ in range(5):
    print(stack.pop())


# Cola / Queue

class Queue():
     
    def __init__(self):
        self.queue = []
        self._first = None
        self.last = None
        
    
    def enqueue(self, element):
        if self.is_empty():
            self.queue.append(element)
            self._first = element
            self.last = element
        else:
            self.queue.insert(0, element)
            self.last = element


    def dequeue(self) -> bool | int:
        if self.is_empty():
            return False

        temp = self.queue.pop()
        self._first = self.queue[-1]
        return temp


    def peek(self) -> int:
        if self.is_empty():
            return -1
        
        return self._first
    
    def size(self):
        return len(self.queue)


    def is_empty(self) -> bool:
        return self.size() == 0
    
    
   
    