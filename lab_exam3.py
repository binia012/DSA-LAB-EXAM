from lab_exam2 import Stack

class LinearQueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        if self.stack1.is_full():
            print("Queue is full")
            return
        self.stack1.push(item)

    def dequeue(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            print("Queue is empty")
            return None
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            print("Queue is empty")
            return None
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()
    

    