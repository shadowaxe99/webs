```python
from flask import Flask, render_template
from src import elysium_os

app = Flask(__name__)

@app.route('/')
def landing_page():
    cityscape = elysium_os.createCityscape()
    virtualHome = elysium_os.integrateAI()
    gamifiedInterface = elysium_os.launchMiniGame()
    aiAgentChat = elysium_os.startChat()
    globalUserBase = elysium_os.showGlobalUserBase()
    aiAssistance = elysium_os.assistAI()
    roadmap = elysium_os.showRoadmap()

    return render_template('landing_page.html', 
                            cityscape=cityscape, 
                            virtualHome=virtualHome, 
                            gamifiedInterface=gamifiedInterface, 
                            aiAgentChat=aiAgentChat, 
                            globalUserBase=globalUserBase, 
                            aiAssistance=aiAssistance, 
                            roadmap=roadmap)

if __name__ == '__main__':
    app.run(debug=True)
```