from passlib.hash import pbkdf2_sha256 as sha256
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['polling_db']
users_collection = db['users']

class User:
    @staticmethod
    def register(username, password):
        if not users_collection.find_one({'username': username}):
            hashed_password = sha256.hash(password)
            users_collection.insert_one({'username': username, 'password': hashed_password})
            return True
        else:
            return False

    @staticmethod
    def authenticate(username, password):
        user = users_collection.find_one({'username': username})
        if user and sha256.verify(password, user['password']):
            return user
        else:
            return None
