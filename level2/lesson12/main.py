class NativeCache:

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        key = str(key)
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
            self.increase_hits(slot_index)
            return True
        return False

    def put(self, key, value):
        slot_index = self.seek_slot(key)
        if slot_index is None:
            slot_index = self.seek_rewrite_slot()

        self.slots[slot_index] = key
        self.values[slot_index] = value
        self.reset_hits(slot_index)

    def get(self, key):
        slot_index = self.seek_slot(key)
        if slot_index is not None:
            self.increase_hits(slot_index)
            return self.values[slot_index]

        return None

    def increase_hits(self, slot_index):
        if self.values[slot_index] is not None:
            self.hits[slot_index] += 1

    def reset_hits(self, slot_index):
        self.hits[slot_index] = 0

    def seek_rewrite_slot(self):
        return self.hits.index(min(self.hits))
