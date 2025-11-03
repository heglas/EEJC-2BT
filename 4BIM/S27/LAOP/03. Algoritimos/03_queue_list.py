class QueueList:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def front(self):
        return self.items[0] if self.items else None

    def isempty(self):
        return not self.items

if __name__ == '__main__':
    queuelist = QueueList()
    queuelist.enqueue(1)
    queuelist.enqueue(2)
    queuelist.enqueue(3)
    print("Fila usando lista:", queuelist.items)
    print("Dequeue:", queuelist.dequeue())
    print("Front:", queuelist.front())