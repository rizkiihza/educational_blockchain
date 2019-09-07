from random import randint

from block_chain import BlockChain
from miner import Miner
from transaction import Transaction

class Main(object):
    def __init__(self):
        return

    def main(self):
        # initiate block chain with num of zero that we want
        block_chain = BlockChain(6)
        miner = Miner(block_chain.hash_processor, block_chain.num_of_zero)

        block_count = 0
        while block_count < 5:
            transaction_list = []

            # generate random transaction
            num_of_transaction = randint(1, 1) 
            for i in range(num_of_transaction):
                transaction_list.append(Transaction(randint(1,100),randint(1,100), randint(200,1000)))

            block = miner.get_new_block(transaction_list, block_chain.get_prev_hash())
            block_chain.add_block(block)

            hash_val = block_chain.hash_processor.calculate_hash(block.get_hash_num())
            print(hash_val)
            print(block)
            print()

            block_count += 1

        print(block_chain.check_is_valid())

        prev_amount = block_chain.blocks[1].transaction_list[0].amount
        block_chain.blocks[1].transaction_list[0].amount = 100800

        print(block_chain.check_is_valid())

        block_chain.blocks[1].transaction_list[0].amount = prev_amount

        print(block_chain.check_is_valid())

if __name__ == '__main__':
    main = Main()
    main.main()

