```python
import json
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['elysium_db']
collection = db['user_feedback']

@app.route('/feedback', methods=['POST'])
def receive_feedback():
    data = request.get_json()
    userFeedback = data['feedback']
    userProgress = data['progress']
    collection.insert_one({"feedback": userFeedback, "progress": userProgress})
    return jsonify({"message": "Feedback received"}), 200

@app.route('/engagement', methods=['GET'])
def get_engagement():
    feedbacks = collection.find()
    feedback_list = []
    for feedback in feedbacks:
        feedback_list.append({"feedback": feedback['feedback'], "progress": feedback['progress']})
    return jsonify({"engagement": feedback_list}), 200

if __name__ == '__main__':
    app.run(debug=True)
```