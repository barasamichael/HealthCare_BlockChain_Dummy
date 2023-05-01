import hashlib
import time

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        hash_data = str(self.index) + str(self.timestamp) + str(self.transactions)\
                + str(self.previous_hash)
        return hashlib.sha256(hash_data.encode()).hexdigest()
