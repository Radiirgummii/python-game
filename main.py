from ursina import Ursina,Entity,color # type: ignore
from ursina.prefabs.platformer_controller_2d import PlatformerController2d# type: ignore
import json

def loadlevel(level):
    for x,row in zip(range(4,-4,-0.5),level["map"]):
        for y, block in zip(range(4,-4,-0.5),row):
            if block != 0:
                Entity(model='quad', scale=(0.5, 0.5), collider='box', color=color.black,y=y,x=x)



with open("assets/levels.json") as f:
    levels = json.load(f)


app = Ursina()


player = PlatformerController2d(y=1, z=.01, scale=0.5, max_jumps=2, jump_height=1, position = (-4, 0))
Ramen = [Entity(model='quad', scale=(9, 0.5), collider='box', color=color.red,y=-4.5),
         Entity(model='quad', scale=(0.5, 9), collider='box', color=color.red,x=-4.5),
         Entity(model='quad', scale=(0.5, 9), collider='box', color=color.red,x=4.5),
         Entity(model='quad', scale=(9, 0.5), collider='box', color=color.red,y=4.5)]
loadlevel(levels["1"])

app.run()