from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()
#EditorCamera()
camera.fov = 100
pl = PlatformerController2d(
    model='quad',
    texture='Assets/그림1.png',
    scale=(2,3),
    position=(2,0),
    origin_y = -0.45,
    collider='box',
    double_sided = True
)

ground = Entity(model='cube',texture = 'Assets/badack.png', y=-5, origin_y=.5, scale=(100,5,5), collider='box', ignore=True)
ground2 = Entity(model='cube',texture = 'Assets/NewPiskel.png', z=10, y=5, origin_y=.5, scale=(100,5,10), collider='box', ignore=True)
cube=Entity(model='cube',texture = 'Assets/badack.png', y=-2, origin_y=.5, scale=(6,2,5), collider='box', ignore=True)
app.run()