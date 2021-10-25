from ursina import *
from ursina import collider
from ursina.prefabs.first_person_controller import FirstPersonController
<<<<<<< HEAD
from ursina.mesh_importer  import *
=======
from dictionaryOfLetters import letter_dictionary
>>>>>>> d08e74a3acbd4dff2d81724f910dba640b9ca97a

app = Ursina()
player = FirstPersonController(collider ='box', speed = 10)

window.fps_counter.enabled = False

model1 = load_model("table v1.obj")
player = Entity(model= model1,
                origin = (0, 0, -3),
                collider = 'box',
                texture = 'white_cube',
                color = color.black)

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
                scale = (100,2,100),
                texture = 'white_cube',
                color = color.color(0, 0, random.uniform(.9, 1.0)),
                collider = 'box',
                texture_scale = (50,50))
Sky()
app.run()

