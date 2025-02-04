Queue.py


from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None


q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  
