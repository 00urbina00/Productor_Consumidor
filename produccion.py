class CircularQueue:
    def __init__(self, size):
        self._size = size            # Size of the queue
        self._queue = [None] * size  # Initialize queue with None
        self._head = 0               # Index of the first element
        self._tail = 0               # Index of the last element
        self._length = 0             # Length of the queue

    @property
    def length(self):
        return self._length
    
    def enqueue(self, item):
        if self._length < self._size:  # Verify if queue is not full
            self._queue[self._tail] = item
            self._tail = (self._tail + 1) % self._size  # Update tail index with circular increment
            self._length += 1
            return True
        else:
            return False  # Queue is full

    def dequeue(self):
        if self._head != self._tail:                          # Queue is not empty 
            item = self._queue[self._head]
            self._queue[self._head] = None
            self._head = (self._head + 1) % self._size
            self._length -= 1                                  # Decrease length
            return item
        else:
            # raise Exception("Queue is empty")
            return None

    def isempty(self):
        if self._head == self._tail:
            return True  # La cola está vacía
        elif self._queue[self._head] is not None:
            return False  # La cola no está vacía
        else:
            return True  # La cola está vacía
    
    def isfull(self):
        next_tail = (self._tail + 1) % self._size
        return next_tail == self._head and self._queue[self._head] is not None
    
    def print_queue(self):
        print()
        for i in range(self._size):
            print(self._queue[i], end=" ")
        print()
            
    def reset(self):
        self._queue = [None] * self._size  # Re - Initialize queue with None
        self._head = 0
        self._tail = 0
        self._length = 0
        
    def clear(self):
        self._queue.clear()
        self._head = 0
        self._tail = 0
        self._length = 0
    

class Production:
    def __init__(self):
        self.state = "working"
        self.number_products = 0
        self.product = 0
        self.position = 0

class Producer(Production):
    def __init__(self):
        super().__init__()
    def get_element(self):
        self.product += 1
        return self.product
        
class Customer(Producer):
    def __init__(self):
        super().__init__()
        

"""
# Caso de prueba
i = 0
queue = CircularQueue(10)
for _ in range(5):
    queue.enqueue(i)
    i += 1
queue.print_queue()
for _ in range(3):
    queue.dequeue()
queue.print_queue()
for _ in range(7):
    queue.enqueue(i)
    i += 1
    
queue.print_queue()
print()

"""