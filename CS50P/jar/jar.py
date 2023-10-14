class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._size = 0

    def __str__(self):
        cookies = ""
        for _ in range(self.size):
            cookies += "🍪"
        return cookies


    def deposit(self, n):
        if n > self._capacity - self._size:
            raise ValueError("Exceed capacity")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size