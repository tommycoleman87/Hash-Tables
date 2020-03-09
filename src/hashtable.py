# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.added_capacity = False
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0
        self.load = None
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for x in key:
            hash = hash * 33 + ord(x)
        return hash 
       


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        if self.storage[self._hash_mod(key)] is None:
            self.storage[self._hash_mod(key)] = LinkedPair(key, value)
            self.count += 1
            self.load = self.count / self.capacity
            if self.load >= .7:
                print(self.load, key)
                self.resize()
        elif self.storage[self._hash_mod(key)].key is key:
            self.storage[self._hash_mod(key)] = LinkedPair(key, value)
        else:
            lp = self.storage[self._hash_mod(key)]
            while lp.next is not None and lp.next.key is not key:
                lp = lp.next
            lp.next = LinkedPair(key, value)
            self.count += 1
            self.load = self.count / self.capacity
            if self.load >= .7:
                print(self.load)
                self.resize()
       



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        lp = self.storage[self._hash_mod(key)]
        if lp == None:
            return 'Error: key not found'
        while lp.key is not key and lp.next is not None:
            if lp.next is not None and lp.next.key is key:
                lp.next = None
                self.count -= 1
                self.load = self.count / self.capacity
                if self.load <= .2 and self.added_capacity is True:
                    self.resize()
            elif lp.next is None:
                return ('error: key not found')
            else:
                lp = lp.next
        if lp.key is key:
            self.storage[self._hash_mod(key)] = None
            self.count -= 1
            self.load = self.count / self.capacity
            if self.load <= .2 and self.added_capacity is True:
                self.resize()
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # print(self.storage[self._hash_mod(key)].value, 'returned value')
        lp = self.storage[self._hash_mod(key)]
        if lp is None:
            return None
        while lp.key is not key and lp.next is not None:
            lp = lp.next
        
        return lp.value
   


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.count = 0
        if self.load >= .7:
            self.capacity = self.capacity * 2
            self.load = self.count / self.capacity
            self.added_capacity = True
        else:
            self.capacity = self.capacity // 2
            self.load = self.count / self.capacity
        self.storage = [None] * self.capacity
        print(len(self.storage))
        for node in old_storage:
            while node:
                self.insert(node.key, node.value)
                node = node.next





if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
