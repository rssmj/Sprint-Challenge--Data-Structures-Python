class RingBuffer:
    def __init__(self, capacity):
        # implement capacity and empty buffer
        self.capacity = capacity
        self.storage = [0]*capacity
        self.current_node = 0

    def append(self, item):
        # point item to current
        self.storage[self.current_node] = item
        # check capacity to set position 
        if self.current_node >= len(self.storage) - 1:
            self.current_node = 0
        # else set increment position
        else:
            self.current_node = self.current_node + 1
    
    def get(self):
        # return buffer contents
        return [item for item in self.storage if item != 0]
        