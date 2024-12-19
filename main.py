#task1
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()
stack.push(10)
stack.push(20)
stack.pop()

#task2
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self, capacity):
        return len(self.queue) >= capacity

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def display(self):
        return self.queue

queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.dequeue()

#task3
import heapq

class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.capacity

    def enqueue(self, item, priority):
        if not self.is_full():
            heapq.heappush(self.queue, (-priority, item))

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0][1]
        return None

    def display(self):
        return [item[1] for item in sorted(self.queue, reverse=True)]

priority_queue = PriorityQueue(5)
priority_queue.enqueue('Task1', 2)
priority_queue.enqueue('Task2', 3)
priority_queue.dequeue()
