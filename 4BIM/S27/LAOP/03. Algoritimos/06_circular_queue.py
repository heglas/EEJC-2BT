class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = self.rear = -1

    def isfull(self):
        return (self.rear + 1) % self.capacity == self.front

    def isempty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.isfull():
            raise OverflowError("Queue overflow")
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.isempty():
            raise IndexError("Queue underflow")
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def frontelement(self):
        return None if self.isempty() else self.queue[self.front]

if __name__ == '__main__':
    cq = CircularQueue(3)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    print("Fila circular após enqueues:", cq.queue)
    try:
        cq.enqueue(40)
    except OverflowError as e:
        print(e)
    print("Elemento removido (dequeue):", cq.dequeue())
    print("Fila circular após dequeue:", cq.queue)
    print("Elemento na frente (front):", cq.frontelement())