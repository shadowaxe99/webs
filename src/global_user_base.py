```python
import three
from websocket import create_connection

class GlobalUserBase:
    def __init__(self):
        self.ws = create_connection("ws://elysiumos.com/realtime")
        self.globe = three.SphereGeometry(50, 50, 50)
        self.material = three.MeshBasicMaterial({ 'color': 0xFFFFFF, 'wireframe': True })
        self.earth = three.Mesh(self.globe, self.material)

    def onMouseMove(self, event):
        raycaster = three.Raycaster()
        mouse = three.Vector2()

        mouse.x = (event.clientX / window.innerWidth) * 2 - 1
        mouse.y = - (event.clientY / window.innerHeight) * 2 + 1

        raycaster.setFromCamera(mouse, camera)
        intersects = raycaster.intersectObjects(scene.children)

        for intersect in intersects:
            if intersect.object == self.earth:
                self.showTooltip(intersect.point)

    def showTooltip(self, point):
        # Fetch data from the server
        self.ws.send(str(point))
        result = self.ws.recv()

        # Display the tooltip
        tooltip = document.getElementById('tooltip')
        tooltip.style.left = event.clientX + 'px'
        tooltip.style.top = event.clientY + 'px'
        tooltip.innerHTML = result

    def update(self):
        # Update the globe with real-time data
        self.ws.send("update")
        result = self.ws.recv()

        for node in result:
            self.earth.add(node)

globalUserBase = GlobalUserBase()
```