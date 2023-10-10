```python
import requests
import json

class ElysiumAPI:
    def __init__(self):
        self.base_url = "https://api.elysium.com"

    def get_cityscape_data(self):
        response = requests.get(f"{self.base_url}/cityscape")
        return response.json()

    def get_ai_integration_data(self):
        response = requests.get(f"{self.base_url}/ai-integration")
        return response.json()

    def get_gamified_interface_data(self):
        response = requests.get(f"{self.base_url}/gamified-interface")
        return response.json()

    def get_ai_agent_chat_data(self):
        response = requests.get(f"{self.base_url}/ai-agent-chat")
        return response.json()

    def get_global_user_base_data(self):
        response = requests.get(f"{self.base_url}/global-user-base")
        return response.json()

    def get_ai_assistance_data(self):
        response = requests.get(f"{self.base_url}/ai-assistance")
        return response.json()

    def get_roadmap_data(self):
        response = requests.get(f"{self.base_url}/roadmap")
        return response.json()

elysium_api = ElysiumAPI()
threeJSModel = elysium_api.get_cityscape_data()
elysiumOS = elysium_api.get_ai_integration_data()
userProgress = elysium_api.get_gamified_interface_data()
userFeedback = elysium_api.get_ai_agent_chat_data()
```