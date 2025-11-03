class StackList:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def isempty(self):
        return not self.items

if __name__ == '__main__':
    stacklist = StackList()
    stacklist.push(1)
    stacklist.push(2)
    stacklist.push(3)
    print("Pilha usando lista:", stacklist.items)
    print("Pop:", stacklist.pop())
    print("Peek:", stacklist.peek())