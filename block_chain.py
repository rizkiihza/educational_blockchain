from block import Block
from transaction import Transaction
from hash_processor import HashProcessor

class BlockChain(object):
    def __init__(self, num_of_zero=4):
        self.num_of_zero = num_of_zero

        self.hash_processor = HashProcessor(61, 100234001241991)

        self.blocks = [] 

    def add_block(self, block):
        # calculate hash of block
        hash_val = self.hash_processor.calculate_hash(block.get_hash_num())
        if hash_val % (10 ** self.num_of_zero) != 0:
            raise Exception("cannot commit transaction hash is wrong")
        elif len(self.blocks) > 0 and block.prev_hash != self.blocks[-1].current_hash:
            raise Exception("wrong prev hash")

        self.blocks.append(block)

    def get_prev_hash(self):
        if len(self.blocks) == 0:
            return None
        else:
            return self.blocks[-1].current_hash

    def check_is_valid(self):
        if len(self.blocks) == 0:
            return True

        for i in range(len(self.blocks) - 1, 0, -1):
            hash_val = self.hash_processor.calculate_hash(self.blocks[i].get_hash_num())

            if hash_val % (10 ** self.num_of_zero) != 0:
                return False

            if self.blocks[i].prev_hash != self.blocks[i-1].current_hash:
                return False

        hash_val_first = self.hash_processor.calculate_hash(self.blocks[0].get_hash_num())

        if hash_val_first % (10 ** self.num_of_zero) != 0:
            return False

        return True



