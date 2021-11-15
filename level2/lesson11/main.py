class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bitmap = 0

    def hash_code(self, key, salt):
        code = 0
        for c in key:
            code = (code * salt + ord(c)) % self.filter_len
        return code

    def hash_bitmask(self, key):
        return (1 << self.hash1(key)) | (1 << self.hash2(key))

    def hash1(self, str1):
        salt = 17
        return self.hash_code(str1, salt)

    def hash2(self, str1):
        salt = 223
        return self.hash_code(str1, salt)

    def add(self, str1):
        bitmask = self.hash_bitmask(str1)
        self.bitmap = self.bitmap | bitmask

    def is_value(self, str1):
        bitmask = self.hash_bitmask(str1)
        return bitmask == self.bitmap & bitmask
