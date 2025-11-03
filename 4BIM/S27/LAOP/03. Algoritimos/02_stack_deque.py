from collections import deque

class StackDeque:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def isempty(self):
        return not self.items

if __name__ == '__main__':
    stackdeque = StackDeque()
    stackdeque.push(1)
    stackdeque.push(2)
    stackdeque.push(3)
    print("Pilha usando deque:", list(stackdeque.items))
    print("Pop:", stackdeque.pop())
    print("Peek:", stackdeque.peek())