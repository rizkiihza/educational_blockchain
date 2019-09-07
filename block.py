from transaction import Transaction

class Block(object):
    def __init__(self):
        self.prev_hash = None
        self.transaction_list = []
        self.current_hash = None

        # hash property
        self.multiply_modulo = 31
        self.divide_modulo = 2402304821

    def get_hash_num(self):
        total = 0

        if self.prev_hash is not None:
            for c in str(self.prev_hash):
                total = total * self.multiply_modulo + ord(c)
                total = total % self.divide_modulo

        for transaction in self.transaction_list:
            total = total * self.multiply_modulo + transaction.get_hash_num()
            total = total % self.divide_modulo

        if self.current_hash is not None:
            for c in str(self.current_hash):
                total = total * self.multiply_modulo + ord(c)
                total = total % self.divide_modulo

        return total

    def add_all_transaction(self, transaction_list):
        for transaction in transaction_list:
            self.transaction_list.append(transaction)

    def __repr__(self):
        return "(prev_hash=%d,transactions=%s,current_hash=%d)" % (self.prev_hash if self.prev_hash is not None else -1 \
                , str(self.transaction_list), self.current_hash)
