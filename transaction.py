
class Transaction(object):
    def __init__(self, 
            from_id,
            to_id,
            amount):

        self.from_id = from_id
        self.to_id = to_id
        self.amount = amount

        # hash atribute
        self.multiply_modulo = 41
        self.divide_modulo = 4312382221

    def get_hash_num(self):
        total = 0

        total = total * self.multiply_modulo + self.from_id
        total = total * self.multiply_modulo + self.to_id

        total = total * self.multiply_modulo + self.amount

        return (total * self.multiply_modulo) % self.divide_modulo

    def __repr__(self):
        return "(from_id=%d,to_id=%d,amount=%d)" % (self.from_id, self.to_id, self.amount)
