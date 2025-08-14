from ursina import *

app = Ursina()

# Simple test scene
Entity(model='cube', color=color.orange, scale=(2, 2, 2))
camera.position = (0, 10, -30)
camera.look_at(Vec3(0, 0, 0))

app.run()
