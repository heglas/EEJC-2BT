class Stack:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def push(self, item):
        if len(self.items) == self.capacity:
            raise OverflowError("Stack overflow")
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Stack underflow")
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.items else None

    def isempty(self):
        return len(self.items) == 0

    def isfull(self):
        return len(self.items) == self.capacity

if __name__ == '__main__':
    stack = Stack(3)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Pilha após pushes:", stack.items)
    try:
        stack.push(40)
    except OverflowError as e:
        print(e)
    print("Elemento removido (pop):", stack.pop())
    print("Pilha após pop:", stack.items)
    try:
        stack.pop()
        stack.pop()
        stack.pop()
    except IndexError as e:
        print(e)