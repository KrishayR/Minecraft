from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

game = Ursina()

grass = load_texture('grass.png')
brick = load_texture('brick.png')
dirt = load_texture('dirt.png')
stone = load_texture('stone.png')
diamond = load_texture('diamond.png')
gold = load_texture('gold.png')
sky = load_texture('sky.png')
sky2 = load_texture('sky2.png')
sky3 = load_texture('sky3.png')
basketball = load_texture('basketball.png')
soccer = load_texture('soccer.png')
marble = load_texture('marble.png')
lapiz = load_texture('lapiz.png')
lava = load_texture('lava.png')
warriors = load_texture('warriors.png')

punch = Audio('sounds/punch.wav', loop = False, autoplay = False)


ambient = Audio('sounds/ambient/rain.wav', loop = True, autoplay = False)

music = Audio('herbal.mp3', loop = True, autoplay = False)
music.play()

block_pick = 1

def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
    if held_keys['7']: block_pick = 7
    if held_keys['8']: block_pick = 8
    if held_keys['9']: block_pick = 9
    if held_keys['0']: block_pick = 0
    if held_keys['l']: block_pick = 10
    if held_keys['y']: block_pick = 11
class Block(Button):
    def __init__(self, position = (0,0,0), texture = grass):
        super().__init__(parent = scene, position = position, model = 'block', origin_y = 0.5, texture = texture, color = color.color(0, 0, random.uniform(0.8, 1)), scale = 0.5)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch.play()
                if block_pick == 1: block = Block(position = self.position + mouse.normal, texture = grass)
                if block_pick == 2: block = Block(position = self.position + mouse.normal, texture = brick)
                if block_pick == 3: block = Block(position = self.position + mouse.normal, texture = stone)
                if block_pick == 4: block = Block(position = self.position + mouse.normal, texture = dirt)
                if block_pick == 5: block = Block(position = self.position + mouse.normal, texture = diamond)
                if block_pick == 6: block = Block(position = self.position + mouse.normal, texture = gold)
                if block_pick == 7: block = Sphere(position = self.position + mouse.normal, texture = basketball)
                if block_pick == 8: block = Sphere(position = self.position + mouse.normal, texture = soccer)
                if block_pick == 9: block = Block(position = self.position + mouse.normal, texture = marble)
                if block_pick == 0: block = Block(position = self.position + mouse.normal, texture = lapiz)
                if block_pick == 10: block = Block(position = self.position + mouse.normal, texture = lava)
                if block_pick == 11: block = Block(position = self.position + mouse.normal, texture = warriors)


            if key == 'right mouse down':
                punch.play()
                destroy(self)

class Sky(Entity):
     def __init__(self):
        super().__init__(parent = scene, model = 'sphere', texture = random.choice([sky, sky2, sky3]), scale = 150, double_sided = True)



for z in range(20):
    for x in range(20):
        block = Block(position = (x, 0, z))

player = FirstPersonController()
sky = Sky()
ambient.play()
game.run()
