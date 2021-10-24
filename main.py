from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from dictionaryOfLetters import letter_dictionary

app = Ursina()
cam = FirstPersonController()

player = Entity(model='cube',
                origin = (0, 0, -3),
                parent = cam)


class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
        )

for z in range(100):
    for x in range(3):
        voxel = Voxel(position=(x,0,z))


app.run()

