#inPyglet.py

import pyglet
from pyglet.window import key

window = pyglet.window.Window()
image = pyglet.resource.image('der1.png')

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        velx=-5
    if symbol == key.D:
        velx=5
    if symbol == key.W:
        vely=5
    if symbol == key.S:
        vely=-5
    
@window.event
def on_draw():
    global posx,posy
    window.clear()
    posx+=velx
    posy+=vely
    image.blit(posx, posy)
    label.draw()
    print(velx)

velx=0
vely=0
posx=0
posy=0
pyglet.app.run()

