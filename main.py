from ursina import *
from ursina import collider
from ursina.prefabs.first_person_controller import FirstPersonController

from ursina.mesh_importer  import *
from dictionaryOfLetters import letter_dictionary

app = Ursina()
player = FirstPersonController(collider = 'box', speed = 10, origin = (-72,-72,0), scale=0.25)

window.fps_counter.enabled = False

model1 = load_model("table v1.obj")
table = Entity(model= model1,
                origin = (0,0,0),
                texture = 'white_cube',
                scale = .0125,
                color = color.green,
                rotation = Vec3(-90,90,0))

table.collider = MeshCollider(table, mesh=table.model, center=Vec3(0,0,0))
table.collider.visible = True

#camera.parent = player

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'sphere',
            origin_y = .5,
            texture = 'white_cube',
            collider = 'box',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
        )


ground = Entity(model = 'plane',
                scale = (72,2,72),
                texture = 'white_cube',
                color = color.color(0, 0, random.uniform(.9, 1.0)),
                collider = 'box',
                texture_scale = (50,50))

class Tower():
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            origin_y = .5,
            texture = 'white_cube',
            collider = 'box',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
        )

        for i in range(0,2):
            for j in range(0,2):
                for k in range(0,3):
                    pass
    
Sky()
app.run()

