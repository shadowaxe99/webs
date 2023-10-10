```python
import requests
import json

class ElysiumAIChat:
    def __init__(self):
        self.chat_history = []
        self.elysiumOS = None

    def start_chat(self):
        print("Welcome to Elysium AI Chat!")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                break
            response = self.get_response(user_input)
            print("Elysium AI: ", response)

    def get_response(self, user_input):
        self.chat_history.append(user_input)
        # Here we simulate the AJAX call to the server to get the AI response
        # In a real-world scenario, this would be replaced with an actual AJAX call
        response = "I'm sorry, I didn't understand that. Could you please rephrase?"
        self.chat_history.append(response)
        return response

    def save_chat(self):
        with open('chat_history.json', 'w') as f:
            json.dump(self.chat_history, f)

    def load_chat(self):
        with open('chat_history.json', 'r') as f:
            self.chat_history = json.load(f)

if __name__ == "__main__":
    chat = ElysiumAIChat()
    chat.start_chat()
    chat.save_chat()
```