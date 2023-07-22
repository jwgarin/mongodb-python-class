from pymongo import MongoClient
import json
import os
import base64
import logging

# Logger settings
logger = logging.getLogger('mongodb')
# Add warning handler
i_handler = logging.StreamHandler()
i_handler.setLevel(logging.INFO)
i_handler.setFormatter(" %(name)s - %(levelname)s - %(message)s ")
logger.addHandler(i_handler)
# Add error handler
e_handler = logging.FileHandler('error.log')
e_handler.setLevel(logging.ERROR)
e_handler.setFormatter(" %(asctime)s - %(name)s - %(levelname)s - %(message)s ")
logger.addHandler(e_handler)


class MongoDB:
    """Pymongo Wrapper for Job parse"""
    def __init__(self, connection_string, db='rivelio', collection='records_psicolo'):
        self.client = connection_string
        self.db = db
        self.collection = collection
    
    @property
    def collection(self):
        return self._collection
    
    @collection.setter
    def collection(self, value):
        self._collection = getattr(self.db, value)
    
    @property
    def db(self):
        return self._db
    
    @db.setter
    def db(self, value):
        self._db = getattr(self.client, value)
    
    @property
    def client(self):
        return self._client
    
    @client.setter
    def client(self, value):
        self._client = MongoClient(value)
        try:
            self.client.admin.command('ping')
            print("Pinged deployment. You successfully connected to MongoDB!")
        except Exception as exc:
            logging.error(exc)
    
    def get(self, filename):
        # Returns empty if not exists and returns the data if exists
        assert os.path.exists(filename), 'file not found: {}'.format(filename)
        with open(filename, 'rb') as f:
            data_bytes = f.read()
            data_base64_bytes = base64.b64encode(data_bytes)
            data_base64_str = data_base64_bytes.decode('ascii')
        return self.collection.find_one({'data': data_base64_str})
    
    def insert(self, record):
        try:
            self.collection.insert_one(record)
        except Exception as exc:
            raise Exception(exc)
    
    def update(self, record_id, update_obj):
        self.collection.update_one({'id': record_id}, {"$set": update_obj})


if __name__ == "__main__":
    with open('settings.json', encoding='utf-8') as f:
        conf = json.load(f)
        connection_string = 'mongodb+srv://{}:{}@cluster83698.b7da08u.mongodb.net/?retryWrites=true&w=majority'.format(*conf['mongodb'].split('|'))
    
    self = MongoDB(connection_string)
    