from random import randint
from time import sleep
from common import Model
################### CONTROLLER #############################

class Controller():
    def __init__(self, m):
        self.m = m
    
    def poll(self):
        cmd = None
        direction = randint(0,3)
        if direction == 0:
            cmd = 'up'
        elif direction == 1:
            cmd = 'down'
        elif direction == 2:
            cmd = 'left'
        elif direction == 3:
            cmd = 'right'
        if cmd:
            self.m.do_cmd(cmd)

################### VIEW #############################

class View():
    def __init__(self, m):
        self.m = m
        
    def display(self):
        b= self.m.mybox
        x = b[0]
        y = b[1]
        print "Position:" , x, ", " , y
    
################### LOOP #############################

model = Model()
c = Controller(model)
v = View(model)
frame=1
while not model.game_over:
    sleep(0.02)
    c.poll()
    model.update()
    if frame == 50:
        v.display()
        frame = 1
    else:
        frame = frame + 1