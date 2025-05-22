import threading

class GenProdCons:
    def __init__(self, size=10, name=None):
        """Initialize the buffer with given size and optional name"""
        self.size = size  # Maximum capacity
        self.name = name  # Optional name
        self.buffer = []  # Internal storage
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)

    def put(self, item):
        """Add an item to the buffer, blocking if full"""
        with self.not_full:
            while len(self.buffer) >= self.size:
                self.not_full.wait()
            self.buffer.append(item)
            self.not_empty.notify()

    def get(self):
        """Remove and return an item from the buffer, blocking if empty"""
        with self.not_empty:
            while len(self.buffer) == 0:
                self.not_empty.wait()
            item = self.buffer.pop(0)
            self.not_full.notify()
            return item

    def __len__(self):
        """Return the current number of items in the buffer"""
        with self.lock:
            return len(self.buffer)