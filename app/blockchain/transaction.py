import datetime

class Transaction:
    def __init__(self, sender, recipient, medical_data):
        self.sender = sender
        self.recipient = recipient
        self.medical_data = medical_data
        self.timestamp = datetime.datetime.now()