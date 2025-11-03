class CustomerServiceQueue:
    def __init__(self):
        self.queue = []

    def arrive(self, customer):
        self.queue.append(customer)

    def serve(self):
        if self.isempty():
            return None
        return self.queue.pop(0)

    def isempty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    csq = CustomerServiceQueue()
    csq.arrive("Cliente 1")
    csq.arrive("Cliente 2")
    csq.arrive("Cliente 3")
    print("Fila após chegada:", csq.queue)
    print("Atendendo:", csq.serve())
    print("Fila após atender:", csq.queue)