from block import Block
class Miner(object):
    def __init__(self, hash_processor, num_of_required_zero):
        self.hash_processor = hash_processor
        self.num_of_required_zero = num_of_required_zero

    def get_new_block(self, transaction_list, prev_hash):
        block = Block()
        block.prev_hash = prev_hash

        for transaction in transaction_list:
            block.transaction_list.append(transaction)

        block.current_hash = self.mine(block)

        return block

    def mine(self, block):
        found = False
        result = None
        current_try = 0

        while not found:
            block.current_hash = current_try
            hash_num = self.hash_processor.calculate_hash(block.get_hash_num())

            if hash_num % (10 ** self.num_of_required_zero) == 0:
                result = current_try
                found = True
            else:
                current_try += 1

        return result


