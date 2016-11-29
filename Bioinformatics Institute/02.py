class MoneyBox:
    def __init__(self, capacity, counter = 0):
        self.capacity = capacity
        self.counter = counter

    def can_add(self, v):
        return self.capacity - self.counter >= v

    def add(self, v):
        self.counter += v
