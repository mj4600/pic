from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()
#EditorCamera()

a = Entity(
        model='quad',
        texture='Assets/그림1.png',
        scale=(2,3),
        position=(2,0),
        origin_y = -0.45,
        collider='box',
        double_sided = True
)

camera.fov = 100
camera.parent = a

def update():
    if held_keys['right arrow']:
        a.x +=10*time.dt
    if held_keys['left arrow']:
        a.x -=10*time.dt
    if not a.intersects(ground).hit:
        a.y -=10*time.dt
    if held_keys['space']:
        a.y +=2



ground = Entity(model='cube',texture = 'Assets/badack.png', y=-5, origin_y=.5, scale=(100,5,5), collider='box', ignore=True)
ground2 = Entity(model='cube',texture = 'Assets/NewPiskel.png', z=10, y=5, origin_y=.5, scale=(100,5,10), collider='box', ignore=True)
cube=Entity(model='cube',texture = 'Assets/badack.png', y=-2, origin_y=.5, scale=(6,2,5), collider='box', ignore=True)
app.run()