class DB:
    def __init__(self):
        self.storage = {}
        self.temp_storage = None
        self.transaction_in_progress = False

    def begin_transaction(self):
        assert self.transaction_in_progress is False, 'Transaction already in progress!'
        print('Beginning transaction.')
        self.transaction_in_progress = True
        self.temp_storage = {}

    def put(self, key: str, value: int):
        assert self.transaction_in_progress is True, 'Transaction not in progress!'
        self.temp_storage[key] = value
        print('Modified transaction.')

    def get(self, key: str):
        if key in self.storage.keys():
            return self.storage[key]
        else:
            print('No key found, returning null.')
            return None

    def commit(self):
        assert self.transaction_in_progress is True, 'Transaction not in progress!'
        self.storage.update(self.temp_storage)
        self.temp_storage = None
        self.transaction_in_progress = False
        print('Changes committed.')

    def rollback(self):
        assert self.transaction_in_progress is True, 'Transaction not in progress!'
        self.temp_storage = None
        self.transaction_in_progress = False
        print('Changes rolled back.')
