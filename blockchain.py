import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_data = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        hash_code = hashlib.sha256(hash_data.encode()).hexdigest()
        return hash_code

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        previous_hash = previous_block.hash
        new_block = Block(data, previous_hash)
        self.chain.append(new_block)
