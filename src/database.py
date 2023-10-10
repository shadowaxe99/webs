```python
from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['elysium_db']

    def get_user(self, user_id):
        user_data = self.db.users.find_one({'_id': user_id})
        return user_data

    def update_user_progress(self, user_id, progress):
        self.db.users.update_one({'_id': user_id}, {'$set': {'progress': progress}})

    def save_user_feedback(self, user_id, feedback):
        self.db.feedback.insert_one({'user_id': user_id, 'feedback': feedback})

    def get_elysium_os(self):
        elysium_os_data = self.db.elysium_os.find_one()
        return elysium_os_data

database = Database()
```