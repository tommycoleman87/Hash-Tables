class DynamicArray:
    def __init--(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity
    
    def insert(self, index, value):
        if self.count >= self.capacity:
            print("error")
            return
        if index >= self.count:
            print('index out of range')
            return
        
        self.storage[index] = value
        self.count += 1