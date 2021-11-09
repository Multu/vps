class PowerSet:

    def __init__(self):
        self.slots = dict()

    def size(self):
        return len(self.slots)

    def put(self, value):
        key = hash(value)
        self.slots[key] = value

    def get(self, value):
        key = hash(value)
        return key in self.slots

    def remove(self, value):
        if self.get(value):
            self.slots.pop(value)
            return True
        return False

    def sort_by_set_size(self, set2):
        small_set = self
        big_set = set2
        if self.size() > set2.size():
            big_set = self
            small_set = set2
        return small_set, big_set

    def intersection(self, set2):
        new_set = PowerSet()

        small_set, big_set = self.sort_by_set_size(set2)
        for value in small_set.slots.values():
            if big_set.get(value):
                new_set.put(value)

        return new_set

    def union(self, set2):
        small_set, big_set = self.sort_by_set_size(set2)

        new_set = PowerSet()
        new_set.slots = big_set.slots.copy()

        for value in small_set.slots.values():
            if new_set.get(value) is False:
                new_set.put(value)

        return new_set

    def difference(self, set2):
        new_set = PowerSet()
        new_set.slots = self.slots.copy()

        intersect_set = self.intersection(set2)
        for value in intersect_set.slots.values():
            new_set.remove(value)

        return new_set

    def issubset(self, set2):
        for value in set2.slots.values():
            if self.get(value) is False:
                return False
        return True
