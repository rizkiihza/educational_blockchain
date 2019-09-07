from random import randint

from block_chain import BlockChain
from miner import Miner
from transaction import Transaction

class Main(object):
    def __init__(self):
        return

    def main(self):
        # initiate block chain with num of zero that we want for proof of work
        num_of_zero = 5
        block_chain = BlockChain(num_of_zero)
        miner = Miner(block_chain.hash_processor, block_chain.num_of_zero)

        block_count = 0
        while block_count < 5:
            transaction_list = []

            # generate random transaction
            num_of_transaction = randint(1, 1) 
            for i in range(num_of_transaction):
                from_id = randint(1,100)
                to_id = randint(1, 100)
                amount = randint(200, 1000)
                transaction = Transaction(from_id, to_id, amount)
                transaction_list.append(transaction)

            # ask miner to get new block to wrap transactions
            # miner will do brute force in order to get the appropriate hash
            block = miner.get_new_block(transaction_list, block_chain.get_prev_hash())

            # add to block_chain
            # block chain will verify the block
            block_chain.add_block(block)

            # print calculated hash value to user
            # to make sure right number of zero in the hash
            hash_val = block_chain.hash_processor.calculate_hash(block.get_hash_num())
            print("block number %d" % (block_count + 1,))
            print("hash value : " + str(hash_val))
            print("generated block : " + str(block))
            print()

            block_count += 1

        # check mutation validation

        # first should be valid
        print(block_chain.check_is_valid())

        # save current value and change the amount to new one
        prev_amount = block_chain.blocks[1].transaction_list[0].amount
        block_chain.blocks[1].transaction_list[0].amount = 100800

        # check validity again, should be false
        print(block_chain.check_is_valid())

        # change it to original value
        # should be valid again
        block_chain.blocks[1].transaction_list[0].amount = prev_amount


        print(block_chain.check_is_valid())

if __name__ == '__main__':
    main = Main()
    main.main()

