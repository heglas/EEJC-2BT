from collections import deque

class QueueDeque:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if self.items else None

    def front(self):
        return self.items[0] if self.items else None

    def isempty(self):
        return not self.items

if __name__ == '__main__':
    queuedeque = QueueDeque()
    queuedeque.enqueue(1)
    queuedeque.enqueue(2)
    queuedeque.enqueue(3)
    print("Fila usando deque:", list(queuedeque.items))
    print("Dequeue:", queuedeque.dequeue())
    print("Front:", queuedeque.front())