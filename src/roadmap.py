```python
import gsap
from elysium_os import elysiumOS

class Roadmap:
    def __init__(self):
        self.timeline = gsap.TimelineLite()
        self.roadmapElement = document.getElementById('roadmap')

    def loadEvents(self):
        # This function would ideally fetch data from a database or an API
        # For simplicity, we're using a static list of events
        self.events = [
            {"year": 2020, "event": "Elysium OS was born."},
            {"year": 2021, "event": "First integration with AI."},
            {"year": 2022, "event": "Global user base reached 1 million."},
            # Add more events as needed
        ]

    def displayEvent(self, event):
        # Create a new DOM element for the event
        eventElement = document.createElement('div')
        eventElement.innerText = f"{event['year']}: {event['event']}"

        # Append the event to the roadmap
        self.roadmapElement.appendChild(eventElement)

        # Animate the event using GSAP
        self.timeline.from(eventElement, 1, {opacity: 0, y: -50})

    def showRoadmap(self):
        self.loadEvents()

        for event in self.events:
            self.displayEvent(event)

roadmap = Roadmap()
roadmap.showRoadmap()
```