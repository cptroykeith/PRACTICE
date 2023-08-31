from collections import deque

class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        # Move elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        # Add the new element to queue1
        self.queue1.append(x)
        
        # Move elements back from queue2 to queue1
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self):
        return self.queue1.popleft()

    def top(self):
        return self.queue1[0]

    def empty(self):
        return not self.queue1


