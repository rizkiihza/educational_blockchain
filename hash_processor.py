class HashProcessor(object):
    def __init__(self,
            multiply_modulo,
            divide_modulo):
        self.multiply_modulo = multiply_modulo
        self.divide_modulo = divide_modulo

    def calculate_hash(self, hash_num):
        total = 0

        for c in str(hash_num):
            total = total * self.multiply_modulo + ord(c)
            total = total % self.divide_modulo

        return total
