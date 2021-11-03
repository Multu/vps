class NativeDictionary:

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        hash_sum = 0
        for i in range(len(key)):
            hash_sum += ord(key[i])
        return hash_sum % self.size

    def seek_slot(self, key):
        hash_code = self.hash_fun(key)

        slot_index = hash_code
        while True:
            if self.slots[slot_index] is None:
                return slot_index
            if self.slots[slot_index] == key:
                return slot_index

            slot_index = (slot_index + 1) % self.size
            if slot_index == hash_code:
                return None

    def is_key(self, key):
        slot_index = self.seek_slot(key)
        if slot_index is not None and self.slots[slot_index] is not None:
            return True
        return False

    def put(self, key, value):
        slot_index = self.seek_slot(key)
        if slot_index is not None:
            self.slots[slot_index] = key
            self.values[slot_index] = value

    def get(self, key):
        if self.is_key(key) is True:
            slot_index = self.seek_slot(key)
            return self.values[slot_index]
        return None
