# Implement a stack 
"""
push - adds an item to the top of the stack
pop  - removes an item from the top of the stack (and returns the value of that item)
size - returns the size of the stack

"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")