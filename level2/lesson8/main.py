class HashTable:

    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        hash_sum = 0
        for i in range(len(value)):
            hash_sum += ord(value[i])

        hash_code = hash_sum % self.size
        return hash_code

    def seek_slot(self, value):
        hash_code = self.hash_fun(value)

        slot_index = hash_code
        while True:
            if self.slots[slot_index] is None:
                return slot_index

            if self.slots[slot_index] == value:
                return None

            slot_index = (slot_index + self.step) % self.size
            if slot_index == hash_code:
                return None

    def put(self, value):
        slot_index = self.seek_slot(value)
        if slot_index is not None:
            self.slots[slot_index] = value
        return slot_index

    def find(self, value):
        hash_code = self.hash_fun(value)

        slot_index = hash_code
        while True:
            if self.slots[slot_index] == value:
                return slot_index
            if self.slots[slot_index] is None:
                return None

            slot_index = (slot_index + self.step) % self.size
            if slot_index == hash_code:
                return None
