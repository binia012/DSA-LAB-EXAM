class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
    
##test case
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(7)
stack.push(9)

print("Stack after pushing elements:", stack.stack)

popped_item = stack.pop()
popped_item = stack.pop()
popped_item = stack.pop()

print("Stack after removing elements: ", stack.stack)


